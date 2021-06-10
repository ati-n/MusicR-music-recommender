import sys
import dataconv


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    artists = dataconv.artists_pivot.head


if __name__ == "__main__":
    sys.exit(main())
