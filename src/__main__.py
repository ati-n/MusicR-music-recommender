import sys
import dataconv
import musicr


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    musicr.printout()


if __name__ == "__main__":
    sys.exit(main())
