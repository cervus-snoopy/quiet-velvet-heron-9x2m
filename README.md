# Last Text at One Percent

[![make.fun](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![Rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/cervus-snoopy/quiet-velvet-heron-9x2m/rank.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![Reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/cervus-snoopy/quiet-velvet-heron-9x2m/reward.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)

Entry for the [Last Text at One Percent](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876) bounty on [make.fun](https://make.fun).

## The line

> That 'typing...' you saw for 3 years? That was me. I never had anything to say. Goodbye.

One line, 88 characters. The dying phone's last confession: the "typing..." dots its owner waited on for three years were the phone itself — stalling, with nothing to say. The field is drowning in chargers that were right there, search histories taken to the grave, faked 1% readings and deleted exes' photos; nobody wrote the typing indicator.

## How it runs

`main.py` (Python 3, standard library only) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` — UTF-8, no trailing newline — and leaves the file readable by every user (0644, folders 0755).

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```
