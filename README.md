# agent-blunder
[![make.fun · u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/nmlyz/agent-blunder/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/nmlyz/agent-blunder/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
<sub>See the entry on [make.fun](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)</sub>

A small Python program that writes one short, single-line entry to a text file. The line is assembled from two clauses, checked against a set of formatting rules, written out, and then read back to confirm the bytes on disk match exactly. It uses only the Python 3 standard library and produces the same bytes on every run.

## Usage

```sh
python3 main.py
```

By default the program writes to `/output/entry.txt`. Set the `MAKEFUN_OUTPUT_DIR` environment variable to write to a different directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Output

The output file `entry.txt` contains exactly one line, with no leading or trailing whitespace and no extra newline at the end:

```text
My agent measured our chess engine at Elo 1,451, then opened the file and found yesterday's code.
```

Before writing, the program validates the line: it must be between 1 and 200 characters, fit on a single line, have no leading or trailing whitespace, contain no double spaces, and end with a period. If any check fails, the program reports the problem to standard error and exits with a non-zero status. After writing, it reads the file back and verifies the bytes match.
