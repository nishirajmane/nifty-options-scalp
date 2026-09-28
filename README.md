# NIFTY and BANKNIFTY options scalp

A [Codex skill](SKILL.md) that reads **NIFTY 50 or BANKNIFTY** intraday charts and prepares a rule-based **long call or put** scalp plan for the Indian market. It uses 15-minute candles for context, closed 5-minute candles for the trigger, and a 09:15–09:30 IST opening range. The skill name stays `nifty-options-scalp` so existing Codex installations and links continue to work.

> **Research status:** This is a paper-trading candidate. It has **not** shown a positive after-cost edge on historical NIFTY or BANKNIFTY option quotes. It produces conditional plans and can return **no trade**. It does not place orders.

## Install in Codex

Clone the repository into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/nishirajmane/nifty-options-scalp.git ~/.codex/skills/nifty-options-scalp
```

If you installed by cloning, update it later with:

```bash
git -C ~/.codex/skills/nifty-options-scalp pull --ff-only
```

Then open a Codex chat and invoke the skill by name:

```text
Use $nifty-options-scalp to review today's BANKNIFTY 5-minute chart for a long-option scalp.
Give me the current opening range, trigger conditions, invalidation, and no-trade conditions.
```

For a position size, also provide trading equity and current option-chain bid/ask quotes. Without those inputs, the skill should not invent a contract price or lot count. If you are reading an older screenshot, it should give a dated chart review and a conditional plan for the next session.

## What the skill checks

| Stage | Rule |
| --- | --- |
| Context | Confirm date, IST time, 15-minute structure, prior close, and each index's own daily ATR(14). |
| Opening range | Mark the high and low of the three completed 5-minute candles from 09:15 to 09:30. |
| Direction | A closed 5-minute candle must break the range and be on the same side of the prior close. |
| Entry | Wait for a retest of the broken edge within three candles; skip a move that runs without one. |
| Contract | Check the live chain for expiry, delta, spread, depth, and current lot size: normally weekly NIFTY or monthly BANKNIFTY. |
| Exit and risk | Use the written premium exit rules, whole-lot size caps, a daily loss limit, and an 11:45 IST time exit. |

The complete rule set is in [SKILL.md](SKILL.md). The index chart sets direction; an option's actual bid/ask quote determines whether a trade is feasible. Spot-index volume may appear as zero and is not used as volume confirmation. The candidate uses **opening-range levels, prior-session levels, and daily ATR(14)**. The [indicator note](references/indicators.md) explains other factors, optional EMA(20), futures VWAP and India VIX, and why extra indicators are not automatic entry rules.

As of September 2026, [NSE lists weekly NIFTY but monthly BANKNIFTY options](https://www.nseindia.com/static/products-services/equity-derivatives-contract-specifications); [BANKNIFTY weekly options ended in 2024](https://nsearchives.nseindia.com/content/circulars/FAOP64506.pdf). Both indices need their own ATR and contract checks. Current exchange files and live quotes always govern a proposed order.

## Example: a valid **no-trade** result

On **28 September 2026**, NIFTY fell below its 09:15–09:30 opening-range low and continued lower. The 5-minute chart did not show the required prompt retest of that level. Under this skill's rules, the result for that move is **no entry**, even though the index later closed near its low. Those historical price levels must not be reused in a new session.

## Evidence and limits

The [29 September 2026 backtest audit](references/backtest-audit-2026-09-29.md) records the recent 5-minute spot signal scan and the limits found in free options replay tools. It includes a [reproducible scan script](scripts/spot_signal_audit.py). The option strategy remains unvalidated.

The [evidence note](references/evidence.md) records the chart review and data sources. The descriptive scan covered **6,642 daily NIFTY rows from 2000–2026**. A recent 5-minute **spot-index** diagnostic covered 41 complete sessions each for NIFTY and BANKNIFTY. Its simpler opening-range-break rule was **not** the retest strategy in this skill. Neither dataset contains the historical option bid/ask fills needed to establish after-cost performance. In that short window, BANKNIFTY's median opening range was **0.425%** of its open versus **0.288%** for NIFTY; this supports separate volatility normalization, not a claim that either strategy works.

Before anyone calls the setup validated, test it separately on point-in-time NIFTY and BANKNIFTY spot and option quotes, with historical expiries, lot sizes, transaction charges, taxes, spread, and slippage. Fix the rules before an out-of-sample test, then report net expectancy, trade count, drawdown, and sensitivity to worse fills. Exchange rules and charges should be checked again when used; see [NSE contract specifications](https://www.nseindia.com/static/products-services/equity-derivatives-contract-specifications), [NSE market timings](https://www.nseindia.com/static/market-data/market-timings), and [Zerodha charges](https://zerodha.com/charges).

## Repository layout

```text
SKILL.md                 Codex instructions and the full candidate setup
agents/openai.yaml       Skill display metadata
references/evidence.md   Source data, observed results, and validation limits
references/backtest-audit-2026-09-29.md  Recent retest scan and platform checks
references/indicators.md Indicator choices and other market/option factors
scripts/spot_signal_audit.py          Reproducible recent spot-index scan
CONTRIBUTING.md          How to propose a change
```

## Contribute

[Open an issue](https://github.com/nishirajmane/nifty-options-scalp/issues) to discuss a finding, or [submit a pull request](https://github.com/nishirajmane/nifty-options-scalp/pulls). Strategy changes are most useful when they include reproducible data, exact rules, costs, and out-of-sample results. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

No license has been selected yet. Please discuss licensing with the repository owner before redistributing the skill outside GitHub.
