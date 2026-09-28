# NIFTY options scalp skill

A Codex skill for reviewing NIFTY 50 intraday charts and preparing a rule-based, risk-sized long-options scalp plan. The setup uses a 15-minute context chart, completed 5-minute candles, and an opening-range break with a retest.

**Status:** research and paper trading. The rules have not been validated on historical option bid/ask quotes after costs. The [evidence note](references/evidence.md) explains the data used and the validation gap. This repository does not place trades.

## Use in Codex

Clone this repository into your Codex skills folder as `nifty-options-scalp`, then ask Codex to use `$nifty-options-scalp` on a current NIFTY chart. Read [SKILL.md](SKILL.md) for the full rules. A screenshot alone cannot establish a live signal or an option's executable price.

## Improve it

Issues and pull requests are welcome. The most useful next contribution is a reproducible, point-in-time test using NIFTY spot candles **and** actual option bid/ask quotes, with historical contract expiries, lot sizes, fees, taxes, and slippage. See [CONTRIBUTING.md](CONTRIBUTING.md) for what to include with a proposed rule change.
