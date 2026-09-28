import datetime as dt
import json
import urllib.parse
import urllib.request
import bisect

UTC = dt.timezone.utc
IST = dt.timezone(dt.timedelta(hours=5, minutes=30))
END = dt.datetime(2026, 9, 29, tzinfo=UTC)

def fetch(symbol, interval, start):
    query = urllib.parse.urlencode({'period1': int(start.timestamp()), 'period2': int(END.timestamp()), 'interval': interval})
    url = 'https://query1.finance.yahoo.com/v8/finance/chart/' + urllib.parse.quote(symbol, safe='') + '?' + query
    request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = json.load(urllib.request.urlopen(request, timeout=30))['chart']['result'][0]
    quote = data['indicators']['quote'][0]
    rows = []
    for i, timestamp in enumerate(data['timestamp']):
        if any(quote[key][i] is None for key in ('open', 'high', 'low', 'close')):
            continue
        rows.append({'at': dt.datetime.fromtimestamp(timestamp, UTC).astimezone(IST), **{key: quote[key][i] for key in ('open', 'high', 'low', 'close')}})
    return rows

def check(symbol):
    daily = fetch(symbol, '1d', dt.datetime(2025, 9, 1, tzinfo=UTC))
    daily_by_date = {row['at'].date(): row for row in daily}
    dates = sorted(daily_by_date)
    atr_by_date = {}
    atr = None
    for i, day in enumerate(dates):
        if i == 0:
            continue
        row, previous = daily_by_date[day], daily_by_date[dates[i - 1]]
        tr = max(row['high'] - row['low'], abs(row['high'] - previous['close']), abs(row['low'] - previous['close']))
        atr = tr if atr is None else (13 * atr + tr) / 14
        if i >= 14:
            atr_by_date[day] = atr
    bars = fetch(symbol, '5m', dt.datetime(2026, 7, 31, tzinfo=UTC))
    by_date = {}
    for bar in bars:
        if dt.time(9, 15) <= bar['at'].time() <= dt.time(15, 25):
            by_date.setdefault(bar['at'].date(), []).append(bar)
    results = []
    trigger_details = []
    full = 0
    for day, session in sorted(by_date.items()):
        prior_index = bisect.bisect_left(dates, day) - 1
        if len(session) < 75 or session[0]['at'].time() != dt.time(9, 15) or session[-1]['at'].time() != dt.time(15, 25) or prior_index < 0 or dates[prior_index] not in atr_by_date:
            continue
        full += 1
        prior_date = dates[prior_index]
        prior = daily_by_date[prior_date]['close']
        opening = [bar for bar in session if dt.time(9, 15) <= bar['at'].time() < dt.time(9, 30)]
        if len(opening) != 3:
            continue
        high, low = max(bar['high'] for bar in opening), min(bar['low'] for bar in opening)
        if high - low > .8 * atr_by_date[prior_date]:
            results.append((str(day), 'range-skip'))
            continue
        outcome = 'no-break'
        for i, bar in enumerate(session):
            if not dt.time(9, 30) <= bar['at'].time() <= dt.time(11, 30):
                continue
            side = 1 if bar['close'] > high and bar['close'] > prior else -1 if bar['close'] < low and bar['close'] < prior else 0
            if side == 0:
                continue
            outcome = 'break-no-retest'
            edge = high if side == 1 else low
            for j in range(i + 1, min(i + 4, len(session))):
                retest = session[j]
                if side == 1 and retest['close'] <= edge or side == -1 and retest['close'] >= edge:
                    break
                touch = retest['low'] <= edge if side == 1 else retest['high'] >= edge
                if not touch:
                    continue
                outcome = 'retest-no-trigger'
                for k in range(j + 1, len(session)):
                    trigger = session[k]
                    if trigger['at'].time() > dt.time(11, 30):
                        break
                    if side == 1 and trigger['close'] <= edge or side == -1 and trigger['close'] >= edge:
                        break
                    crossed = trigger['high'] > retest['high'] if side == 1 else trigger['low'] < retest['low']
                    if crossed:
                        outcome = 'call-trigger' if side == 1 else 'put-trigger'
                        record = {'date': str(day), 'side': 'call' if side == 1 else 'put', 'break_bar_start_ist': bar['at'].strftime('%H:%M'), 'retest_bar_start_ist': retest['at'].strftime('%H:%M'), 'trigger_bar_start_ist': trigger['at'].strftime('%H:%M'), 'trigger_level': round(retest['high'] if side == 1 else retest['low'], 2), 'opening_high': round(high, 2), 'opening_low': round(low, 2)}
                        if k + 1 < len(session) and session[k + 1]['at'].time() <= dt.time(11, 45):
                            entry = session[k + 1]
                            if side * (entry['open'] - (retest['high'] if side == 1 else retest['low'])) <= 0:
                                record['proxy_status'] = 'next open no longer beyond trigger; no proxy entry'
                            else:
                                exit_bar = next((x for x in session[k + 1:] if x['at'].time() <= dt.time(11, 40) and ((side == 1 and x['close'] <= high) or (side == -1 and x['close'] >= low))), None)
                                exit_next = session[session.index(exit_bar) + 1] if exit_bar is not None and session.index(exit_bar) + 1 < len(session) else next((x for x in session if x['at'].time() == dt.time(11, 45)), None)
                                if exit_next is not None:
                                    record.update({'proxy_entry_ist': entry['at'].strftime('%H:%M'), 'proxy_exit_ist': exit_next['at'].strftime('%H:%M'), 'proxy_entry_index': round(entry['open'], 2), 'proxy_exit_index': round(exit_next['open'], 2), 'proxy_directional_points': round(side * (exit_next['open'] - entry['open']), 2), 'proxy_exit_reason': 'range invalidation' if exit_bar is not None else '11:45 cutoff'})
                        trigger_details.append(record)
                        break
                break
            break
        results.append((str(day), outcome))
    from collections import Counter
    return {'symbol': symbol, 'full_sessions': full, 'outcomes': dict(Counter(outcome for _, outcome in results)), 'triggers': trigger_details}

if __name__ == '__main__':
    print(json.dumps([check('^NSEI'), check('^NSEBANK')], indent=2))
