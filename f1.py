import requests
import argparse
import sys

### API Calls ###

def get_standings() -> list:
    try:
        response = requests.get("https://api.jolpi.ca/ergast/f1/2026/driverstandings/", timeout=(10,20))
        data = response.json()
        return data["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Error: could not connect to the F1 API. Check your internet connection.")
    except KeyError:
        raise KeyError("Error: unexpected response from the F1 API.")

def get_race(choice) -> str:
    try:
        response = requests.get("https://api.jolpi.ca/ergast/f1/2026/races/")
        data = response.json()
        races = data["MRData"]["RaceTable"]["Races"]

        if choice <= len(races) and choice >= 1:
            return races[choice-1]["raceName"]
        return "Race not found."
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Error: could not connect to the F1 API. Check your internet connection.")
    except KeyError:
        raise KeyError("Error: unexpected response from the F1 API.")

### Data Printing ###

def run_standings(args) -> None:
    drivers = get_standings()
    for driver in drivers:
        print(f"{driver['position']}. {driver['Driver']['givenName']} {driver['Driver']['familyName']} - {driver['points']} pts ({driver['Constructors'][0]['name']})")

def run_race(args) -> None:
    print(get_race(args.race))

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
            run_standings(args)
        if args.race is not None:
            run_race(args)
    except ConnectionError as e:
        print(e)
        sys.exit(1)
    except KeyError as e:
        print (e)
        sys.exit(1)

if __name__ == "__main__":
    main()