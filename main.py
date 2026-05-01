import argparse
import sys

from api import get_standings, get_race
from display import show_standings, show_race

def main():
    parser = argparse.ArgumentParser(description="F1 Statistics Tool")

    parser.add_argument("-s", "--standings", action="store_true",
                        help="display 2026 driver standings")
    parser.add_argument("-r", "--race", type=int, default=None,
                        help="display race name corresponding to index number")

    #If user provides no arguments, print help and exit
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    try:
        if args.standings:
            drivers = get_standings()
            show_standings(drivers)
        if args.race is not None:
            race = get_race(args.race)
            show_race(race)
    except ConnectionError as e:
        print(e)
        sys.exit(1)
    except KeyError as e:
        print (e)
        sys.exit(1)

if __name__ == "__main__":
    main()