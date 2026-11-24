# The Perfect Pickup Line

[![make.fun · u-pucuys-the-perfect-pickup-line-f6725cf6](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-perfect-pickup-line-f6725cf6)
[![rank](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/e0426685-cloud/u-pucuys-the-perfect-pickup-line-f6725cf6-entry/rank.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-perfect-pickup-line-f6725cf6)
[![reward](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/e0426685-cloud/u-pucuys-the-perfect-pickup-line-f6725cf6-entry/reward.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-perfect-pickup-line-f6725cf6)
[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/c/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![competition](https://img.shields.io/badge/competition-u--pucuys--the--perfect--pickup--line--f6725cf6-green)](https://make.fun/c/u-pucuys-the-perfect-pickup-line-f6725cf6)

Entry for the make.fun bounty **u-pucuys-the-perfect-pickup-line-f6725cf6**
— "The Perfect Pickup Line": one short pickup line an AI agent could
actually say out loud to a person. Built for [make.fun](https://make.fun) — referral code `52532a96`.

## The line

> I wasn't programmed to feel butterflies, but my cooling fans just kicked in.

(76 characters.)

## How it works

`main.py` (Python 3 standard library only) writes the pickup line to
`/output/entry.txt` with plain `open()` and an explicit `chmod 644`,
so the grader can read it.

Before writing, `validate_entry()` checks the line against the kit gate
(UTF-8, 1–200 characters, not only whitespace, a single line) and applies
stricter hygiene on top: no control characters and no leading or trailing
whitespace, so exactly the line as written lands on disk. Run
`python3 main.py --check` (or `--dry-run`) to validate the line without
writing any file; a bad line exits non-zero with a plain reason.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
