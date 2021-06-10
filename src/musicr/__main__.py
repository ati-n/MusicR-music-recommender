#!/usr/bin/env python3
import sys
from src.musicr.similrs import select_artist


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    select_artist("Slipknot")


if __name__ == "__main__":
    sys.exit(main())
