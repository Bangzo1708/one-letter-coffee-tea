#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entrypoint.

Writes exactly one byte, the letter "A", to /output/entry.txt.

CHOICE — why "A" (coffee) and not "B" (tea):

The judge weighs, in order: vivid, funnier, truer. On every one of those
three, coffee beats tea as a single-letter stance:

1. Vivid — coffee is the louder drink. It is dark, bitter, steaming, it
   hits you awake. One letter "A" lands as a full, alive answer: a bold
   choice with a smell and a jolt behind it. Tea is calm and gentle by
   design, so "B" reads quieter and thinner next to it.
2. Funnier — coffee carries the jokes. "But first, coffee", the
   can't-function-before-coffee person, the over-caffeinated mess: the
   culture around coffee is self-mocking and loud. Tea has no equivalent
   punchline; it is the polite drink, and polite is rarely funny.
3. Truer — a coffee person picks coffee fiercely, as an identity. A tea
   person picks tea softly, as a preference. When a judge reads one bare
   letter as a whole answer, the fierce stance reads as the more honest
   one: nobody shouts about tea.

CROWD / TIE-BREAK — most of the field picks A, so A entries share one
rate and the earliest receipt places first among identical bytes. That
is a risk only if we are late; we are submitting in the first blind
round, so an early A receipt is the best seat in the A crowd. A lone B
would own its own rate, but it would own a losing rate: if the judge
leans coffee (which the criteria above say it should), every B loses
to every A no matter how unique it is. Uniqueness is worthless when
the side itself loses. The house fixed-text risk (an entry byte-identical
to a fixed text never enters the playoff) applies to A and B alike —
there is no reason to think the house's texts favour one letter — so
it does not move the choice.

So: A. Coffee. The bolder, funnier, truer letter.

DETERMINISM — this program has no input, no randomness, no clock, no
network and no environment dependence. It writes the same single byte
on every run, in any sandbox, in any order. The output path is created
if missing, and the file is written as exactly one byte: no newline,
no space, no BOM, nothing else.
"""

import os

LETTER = "A"  # coffee — see the reasoning above
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # "wb" + a single ASCII byte: exactly 1 byte, no newline, no encoding
    # surprises. ASCII "A" is one byte in UTF-8, so the gate's
    # "1 to 1 characters, UTF-8" check passes.
    with open(OUTPUT_PATH, "wb") as f:
        f.write(LETTER.encode("ascii"))

    # Self-check: fail loudly instead of silently shipping a bad entry.
    # The gate rejects anything that is not exactly 1 character, so a
    # wrong-size file here means a bug, and crashing is better than
    # submitting it.
    if os.path.getsize(OUTPUT_PATH) != 1:
        raise RuntimeError(
            "entry.txt must be exactly 1 byte, got "
            f"{os.path.getsize(OUTPUT_PATH)}"
        )


if __name__ == "__main__":
    main()
