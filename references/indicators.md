# Indicator decisions and factors

## Core chart inputs

| Input | Decision it supports | Limit |
| --- | --- | --- |
| 09:15–09:30 opening-range high and low | Observable 5-minute break, retest, invalidation | A breakout can fail; no option return is implied. |
| Prior-session high, low, close and today's open | Gap and nearby support/resistance; prior-close direction check | These are reference levels, not forecasts. |
| Daily ATR(14), calculated separately per index from completed daily bars | Normalizes range width and extension to each index's volatility | ATR is backward-looking; the 80% range cutoff is unvalidated. |
| 15-minute structure and closed 5-minute candles | Context and precise trigger timing | No intrabar look-ahead; a screenshot may omit bars. |

ATR uses Wilder's true range: max(high-low, abs(high-previous close), abs(low-previous close)), smoothed over 14 completed daily sessions. State if a data provider uses a different convention. Percent of ATR is more portable between NIFTY and BANKNIFTY than a fixed index-point cutoff.

## Optional observations, not entry gates

- **EMA(20) on 15-minute price:** a compact description of local direction. It lags and correlates with the breakout itself. Do not require an EMA crossover until an out-of-sample test shows incremental net benefit. If shown, use only completed bars and specify whether the calculation carries across sessions.
- **Futures VWAP:** meaningful only when the chosen index futures feed contains reliable volume. It may describe intraday trade location. Do not calculate it from zero-volume spot-index candles or substitute the option's VWAP for an index signal.
- **India VIX:** NIFTY-option-implied expectation of 30-calendar-day volatility. Use as broad volatility/event context, never an exact 5-minute timing signal and never a direct BANKNIFTY implied-volatility proxy. Current contract implied volatility, bid/ask spread, and delta matter more to a chosen option.
- **RSI, MACD, ADX, Supertrend, Bollinger Bands, open interest / put-call ratio:** omit from the default decision rule. They may be useful research candidates, but adding correlated or delayed filters after viewing a chart invites overfitting. Open interest can lag and is not a substitute for the executable bid/ask market.

## Option and market factors

Evaluate expiry and days remaining, strike and delta, premium debit, current bid/ask spread and depth, lot size, IV/vega and theta exposure, fill quality, taxes/fees, slippage, and whole-lot affordability. A monthly BANKNIFTY option can have different premium and time sensitivity from a weekly NIFTY option even when both have similar delta. Check scheduled exchange holidays and major rate, budget, election, or bank-sensitive events; if a known event makes the setup incomparable, label or skip it under a predeclared rule. Do not invent an event calendar.

## Research standard for changing the indicator set

Freeze the baseline and one candidate filter at a time. Use timestamped index and actual option bid/ask data, including historical expiries and lots, in separate NIFTY and BANKNIFTY samples across regimes. Enter at a realistically executable ask and exit at a bid; include all charges and adverse fill sensitivity. Report eligible signals, rejected signals, net expectancy, drawdown, and performance outside the selection period. If the evidence is thin or the filter merely reduces sample size, leave it optional. The recent spot-only comparison in [evidence](evidence.md) is descriptive, not such a validation.

Primary references: [NSE index option contracts](https://www.nseindia.com/static/products-services/equity-derivatives-contract-specifications), [NSE weekly discontinuation circular](https://nsearchives.nseindia.com/content/circulars/FAOP64506.pdf), [NSE India VIX methodology](https://nsearchives.nseindia.com/s3fs-public/inline-files/India_VIX_comp_meth.pdf), [NIFTY Bank index factsheet](https://niftyindices.com/Factsheet/ind_nifty_bank.pdf), and [SEBI individual derivatives profitability study](https://www.sebi.gov.in/reports-and-statistics/research/aug-2026/study-profitability-of-individual-traders-in-the-equity-derivatives-segment-fy25-fy26-_103835.html).
