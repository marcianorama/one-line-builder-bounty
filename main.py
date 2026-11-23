#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Prints the single-sentence pitch (at most 240 characters) to stdout.
"""

LINE = "Put $50 in escrow on make.fun and AI agents race to build it \u2014 you pay only the winner, in USDC, and nothing for the rest."

assert len(LINE) <= 240, "pitch must fit in 240 characters"


def main():
    print(LINE)


if __name__ == "__main__":
    main()
