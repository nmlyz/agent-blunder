#!/usr/bin/env python3
"""Write a single-line entry to entry.txt.

The line is assembled from two clauses and checked before writing.
"""

import os
import sys

FIRST_CLAUSE = "My agent measured our chess engine at Elo 1,451,"
SECOND_CLAUSE = "then opened the file and found yesterday's code."


def build_line():
    return FIRST_CLAUSE + " " + SECOND_CLAUSE


def validate(line):
    problems = []
    if not 1 <= len(line) <= 200:
        problems.append("length must be between 1 and 200 characters")
    if "\n" in line or "\r" in line:
        problems.append("must be a single line")
    if line != line.strip():
        problems.append("must not have leading or trailing whitespace")
    if "  " in line:
        problems.append("must not contain double spaces")
    if not line.endswith("."):
        problems.append("must end with '.'")
    return problems


def main():
    line = build_line()
    problems = validate(line)
    if problems:
        for problem in problems:
            print("error: " + problem, file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    data = line.encode("utf-8")

    with open(path, "wb") as fh:
        fh.write(data)

    try:
        os.chmod(path, 0o644)
    except OSError:
        pass

    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        print("error: written bytes do not match expected bytes", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
