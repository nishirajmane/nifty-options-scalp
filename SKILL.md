---
name: nifty-options-scalp
description: Analyze NIFTY 50 intraday charts and prepare a rule-based, risk-sized long-options scalp plan for NSE trading. Use for NIFTY call/put scalp reviews and paper-trading plans; not for other indices or stock options.
---

# NIFTY options scalp

Use the NIFTY 50 spot index for direction, a 15-minute chart for context, and closed 5-minute candles for triggers. The index itself is not tradable; the proposed instrument is a long NIFTY call or put. A screenshot is historical evidence, not a live quote. Do not infer option premium, spread, delta, or profit from index candles.

## Verify the session

- State the chart date, time zone (IST), interval, and whether the market is open. If the chart is stale, give a conditional plan for the next session rather than a live signal.
- Read the current NSE trading calendar, contract specification, expiry, lot size, and broker charges before naming a contract or rupee position size. These can change. Check the actual option chain for bid, ask, depth, delta or an explicitly labeled estimate, and expiry.
- Mark previous session high, low, close; current open; and current 14-day ATR. On each new session, mark the 09:15–09:30 opening range high and low from completed 5-minute bars. Recalculate levels rather than carrying a price from an old screenshot.
- Spot-index volume may display zero. Do not treat it as meaningful volume or calculate spot VWAP from it.

## Candidate setup: opening-range break and retest

This is a **candidate for paper testing**, not a demonstrated edge. Apply the rules without optimizing them from a single chart.

1. Look for entries only from 09:30 to 11:30 IST. For a put, require a completed 5-minute close below the opening-range low and below the prior close. For a call, require a completed 5-minute close above the opening-range high and above the prior close. If the first 15-minute range already exceeds 80% of the 14-day ATR, skip the morning: the stop distance is likely too large for this setup.
2. Wait up to the next three 5-minute candles for a retest of the broken range edge. For a put, the candle may touch the edge but must close below it; enter only when a later candle breaks that retest candle's low. Reverse the rules for a call. If price closes back inside the range, the retest fails. If there is no retest, skip rather than chase.
3. Buy the nearest weekly option with at least two calendar days to expiry, preferably ATM or one strike in the money and approximately 0.45–0.65 absolute delta. On expiry day use a later expiry. Require a live two-sided quote, bid/ask spread no more than 1% of the midpoint, and displayed size at least as large as the planned order. Use a limit order and record the actual fill.
4. Exit when the option bid is 20% below the paid premium, or a completed 5-minute index candle closes back inside the opening range, whichever occurs first. Place a profit limit at 30% above paid premium, subject to a fillable bid. Close any remaining position by 11:45 IST. These are gross premium thresholds; include fees, spread, and slippage in the actual result.
5. Maximum planned loss per idea is 0.25% of trading equity, including estimated round-trip fees and slippage. Also cap total premium paid at 2% of trading equity. Size whole lots by the stricter cap; if even one lot breaches either, report **no trade**. Stop for the day after two losing trades or 0.5% equity lost, whichever comes first. Never average down or carry the scalp overnight.

## Output for a chart review

Give the timestamp and source, trend and nearby levels, the opening range, bullish and bearish trigger conditions, contract-selection criteria, premium-based risk and whole-lot calculation, and a clear status: `setup absent`, `watching`, `candidate triggered`, or `no trade`. Label unobserved data and assumptions. If the user wants a proven strategy, read [evidence and validation](references/evidence.md), explain the current evidence limits, and propose a proper option-quote backtest before treating it as live-ready.
