---
name: nifty-options-scalp
description: Review NIFTY 50 or BANKNIFTY intraday charts and prepare a conditional, risk-sized long call or put scalp plan using current NSE option contracts. Use for Indian index options chart reviews and paper trading plans.
---

# NIFTY and BANKNIFTY options scalp

Use the selected **spot index** for direction, 15-minute candles for context, and completed 5-minute candles for triggers. The indices cannot be bought as options: select an actual NIFTY or BANKNIFTY contract only after checking live quotes. A historical screenshot is never a live signal. Never infer option premium, delta, fill, or profit from index candles.

## Establish the session and instrument

- Identify NIFTY 50 versus BANKNIFTY, chart date, IST time, interval, market state, and data source. For a stale chart give a dated review and next-session conditions.
- Check the current NSE calendar, contract list, expiry, lot size, strike spacing, and broker charges. As of September 2026, NSE lists weekly plus monthly NIFTY options but monthly BANKNIFTY options; Tuesday is the scheduled expiry, advanced for an exchange holiday. Recheck before each use.
- Mark prior high, low, and close; today's open; 14 completed daily bars' ATR; and the 09:15–09:30 opening-range high and low from three completed 5-minute candles. Compute ATR and levels **separately for each index**. Never transplant NIFTY point thresholds to BANKNIFTY.
- Note gaps, nearby prior levels, abnormal news/event risk, and whether the first range consumes much of that index's usual daily movement. If the first range exceeds 80% of the index's ATR, skip this proposed morning setup. The 80% cutoff is unvalidated and should be studied, not treated as an optimized value.
- Spot-index volume may be zero. Do not use it as volume confirmation or compute spot VWAP from it. If reliable NIFTY or BANKNIFTY futures price *and volume* are available, futures VWAP may be reported as secondary context; it is not a required trigger.

## Candidate entry: opening-range break and retest

This is a **paper-testing candidate**, not a demonstrated profitable strategy. Use the same structural rules on either index; keep results and parameters separate by instrument.

1. Consider an entry only from 09:30 to 11:30 IST. For a put, require a completed 5-minute index close below both the opening-range low and prior close. For a call, require a completed close above both the opening-range high and prior close. The 15-minute view should identify nearby opposing levels and whether the move is already extended; do not convert subjective trend impressions into an extra mandatory signal.
2. Within the next three 5-minute candles, require a retest of the broken range edge. For a put, the retest may touch the edge but must close below it; enter only on a later break of that retest candle's low. Reverse for a call. A close back inside the range invalidates the setup. Skip a move without a retest.
3. Select the nearest liquid expiry with at least two calendar days remaining: normally a **weekly NIFTY** or **monthly BANKNIFTY** contract. Use ATM or one strike in the money, with about 0.45–0.65 absolute delta if a trustworthy current value is available. If a delta estimate is used, label it. Require a live two-sided quote, bid/ask spread ≤1% of midpoint, and displayed size sufficient for the planned order. If no eligible contract passes, report `no trade`. Use a limit order and record the actual fill.
4. The candidate exit is the earlier of an option bid 20% below the paid premium or a completed index candle back inside the opening range. A 30% premium gain is the candidate profit exit, subject to a fillable bid. Close by 11:45 IST. These thresholds are hypotheses and may behave differently for monthly BANKNIFTY options; do not describe them as validated on either instrument.
5. Limit planned loss per idea, including estimated round-trip charges and slippage, to 0.25% of trading equity. Cap total premium paid at 2% of equity. Size in current whole lots using the stricter cap; if one lot exceeds either cap, report `no trade`. Stop after two losing trades or 0.5% equity lost in a day. Never average down or carry the scalp overnight.

## Indicator choice and output

The required chart tools are **opening-range levels, prior-session levels, and daily ATR(14)**. These directly define trigger and risk context. An intraday 20-period EMA, futures VWAP, or India VIX can be noted as **secondary context only** when data supports it; none is a proven improvement to this setup. India VIX is based on NIFTY options and is not a BANKNIFTY-specific volatility measure. Do not stack RSI, MACD, ADX, Supertrend, or Bollinger Bands as automatic confirmations without a fixed, after-cost, out-of-sample comparison. See [indicator decisions](references/indicators.md) when asked which indicators to use or to improve the strategy.

Report source and timestamp, selected index, nearby levels and ATR, opening range, long-call and long-put conditions, invalidation, exact contract-selection checks, option-quote-based whole-lot sizing, and status (`setup absent`, `watching`, `candidate triggered`, or `no trade`). Label missing quotes and assumptions. Read [evidence and validation](references/evidence.md) before making performance claims or proposing live deployment.
