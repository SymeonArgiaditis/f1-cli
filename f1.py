import requests
import argparse
import sys

### API Calls ###

def get_standings() -> list: 
    response = requests.get("https://api.jolpi.ca/ergast/f1/2026/driverstandings/")
    data = response.json()
    return data["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]

def get_race(choice) -> list:
    response = requests.get("https://api.jolpi.ca/ergast/f1/2026/races/")
    data = response.json()

    races = data["MRData"]["RaceTable"]["Races"]
    return races[choice-1]["raceName"] if choice <= len(races) and choice >= 1 else "Race not found."

### Data Printing ###

def run_standings(args) -> None:
    drivers = get_standings()
    for driver in drivers:
        print(f"{driver["position"]}. {driver["Driver"]["givenName"]} {driver["Driver"]["familyName"]} - {driver["points"]} pts ({driver['Constructors'][0]['name']})")

def run_race(args) -> None:
    print(get_race(args.race))

def main():
    parser = argparse.ArgumentParser(description="F1 Statistics Tool")

    parser.add_argument("-s", "--standings", action="store_true",
                        help="display 2025 driver standings")
    parser.add_argument("-r", "--race", type=int, default=None,
                        help="display race name corresponding to index number")

    #If user provides no arguments, print help and exit
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    if args.standings:
        run_standings(args)
    if args.race is not None:
        run_race(args)

if __name__ == "__main__":
    main()