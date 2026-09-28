# NIFTY and BANKNIFTY options scalp: backtest audit

**As of:** 29 September 2026, IST
**Result:** Spot-index entry study completed. A faithful historical options P&L backtest was **not** completed. The strategy has no demonstrated after-cost edge.

## Rules examined

The published skill looks for a completed 5-minute close beyond the 09:15–09:30 opening range and previous close, a retest in the next three candles, then a later break of the retest candle's extreme. A range wider than 80% of the prior completed daily ATR(14) is skipped. The intended trade then buys an eligible NIFTY or BANKNIFTY option and exits on a 20% premium loss, 30% premium gain, index close back inside the range, or 11:45 IST. These thresholds were set before this audit and have not been optimized.

## Data and spot-index results

I used Yahoo Finance's 5-minute NIFTY (`^NSEI`) and BANKNIFTY (`^NSEBANK`) spot candles for 31 July–28 September 2026 and completed daily bars for the prior close and ATR. Each index had 40 complete sessions after requiring all 75 five-minute bars from 09:15 to 15:25. The scan considers the first qualifying break in each session and at most one setup per day. Candles are timestamped at their **start** in IST. A 5-minute high or low can show that a level was crossed, but cannot establish the exact time or executable option price of that crossing.

| Index | Complete sessions | Call triggers | Put triggers | Total triggers |
| --- | ---: | ---: | ---: | ---: |
| NIFTY | 40 | 2 | 2 | 4 |
| BANKNIFTY | 40 | 2 | 2 | 4 |

As a deliberately separate **delayed-entry index proxy**, I required the *next* 5-minute candle to open beyond the retest trigger level. I then measured directional index points from that open to the next open after an index close back inside the range, or the 11:45 open. This is not the skill's intrabar option fill rule. It omits the premium stop and target, contract selection, costs, and quote filters.

| Index | Date | Side | Trigger bar | Next-open proxy | Directional index points |
| --- | --- | --- | --- | --- | ---: |
| NIFTY | 17 Aug | Put | 10:20 | Entered 10:25; exit 11:45 | +7.95 |
| NIFTY | 26 Aug | Call | 09:55 | No next-open proxy entry | — |
| NIFTY | 31 Aug | Put | 09:55 | No next-open proxy entry | — |
| NIFTY | 23 Sep | Call | 10:55 | No next-open proxy entry | — |
| BANKNIFTY | 18 Aug | Put | 10:10 | Entered 10:15; invalidated 10:30 | −42.75 |
| BANKNIFTY | 20 Aug | Call | 09:55 | Entered 10:00; exit 11:45 | −31.55 |
| BANKNIFTY | 27 Aug | Put | 10:50 | Entered 10:55; exit 11:45 | −4.55 |
| BANKNIFTY | 16 Sep | Call | 10:50 | Entered 10:55; invalidated 11:15 | −88.00 |

The five next-open proxy observations are too few to estimate expectancy. Index points cannot be translated into option returns. A trigger that reverses before the next open may still have filled under the original intrabar rule; “no proxy entry” does not mean no actual option trade.

## Free-site checks after sign-in

- **[AlgoShot](https://www.algoshot.in/):** I configured an ATM BANKNIFTY call with 10:55 entry, 11:45 exit, +30% target and −20% stop for 16 September 2026. The site rejected the run with: “Unfortunately, we have data for date ranges from Jan 2019 to December 2023 only.” Its visible builder also does not express the spot-index opening-range and retest triggers, the exact expiry rule, or bid/ask liquidity checks.
- **[NiftyTrader Options Simulator](https://www.niftytrader.in/options-simulator):** The signed-in simulator loaded NIFTY for 23 September 2026 and the 29 September expiry. It labels its result **gross LTP P&L excluding slippage**. Its 5-minute replay displayed spot 23,416.70 at 10:55 and 23,414.85 at 11:00, both below the retest trigger of 23,420.75. The signal candle's high crossed that level intrabar, so neither display gives an entry quote at the crossing. Selecting BANKNIFTY opened an Options Simulator Plan paywall. No simulated position was opened, and no profit figure is claimed.
- **[ZeroAlgo](https://zeroalgotest.com/):** Its own product page says account access is manually approved and its current chains cover NIFTY and SENSEX, not BANKNIFTY. It therefore could not provide an immediate two-index check.

## What a valid options backtest still needs

Obtain point-in-time spot candles and the actual eligible option contracts, with timestamped bid/ask and depth, for a longer period across market regimes. Apply the trigger and fills without knowing later candles; use actual historical expiries and lot sizes. Record premium stops and targets, index invalidations, charges, slippage, skipped trades, and whole-lot risk limits. Publish trade-level NIFTY and BANKNIFTY results separately, then test an untouched period and paper-trade live before considering deployment.

**Sources:** [Yahoo NIFTY history](https://finance.yahoo.com/quote/%5ENSEI/history/), [Yahoo BANKNIFTY history](https://finance.yahoo.com/quote/%5ENSEBANK/history/), the directly observed signed-in [AlgoShot builder](https://www.algoshot.in/explore/backtest) and [NiftyTrader simulator](https://www.niftytrader.in/options-simulator), and [ZeroAlgo's published limitations](https://zeroalgotest.com/).
