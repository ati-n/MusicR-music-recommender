import sys
import dataconv
import musicr


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    musicr.select_artist("The Chemical Brothers")


if __name__ == "__main__":
    sys.exit(main())
