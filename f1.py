import requests
import argparse
import sys

###API Calls###

def get_standings() -> list: 
    response = requests.get("https://api.jolpi.ca/ergast/f1/2025/driverStandings/")
    data = response.json()
    drivers = data["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]

    return drivers

def get_race(choice) -> list:
    response = requests.get("https://api.jolpi.ca/ergast/f1/2026/races/")
    data = response.json()

    race = data["MRData"]["RaceTable"]["Races"][choice]["raceName"]
    return race

### Data Printing###

def print_standings(drivers) -> None:
    for driver in drivers:
        print(f"{driver["position"]}. {driver["Driver"]["givenName"]} {driver["Driver"]["familyName"]} - {driver["points"]} pts ({driver['Constructors'][0]['name']})")

def print_race(race) -> None:
    print(race)

def main():
    parser = argparse.ArgumentParser(description="F1 Statistics Tool")

    parser.add_argument("-s", "--standings", action="store_true",
                        help="display 2025 driver standings")
    parser.add_argument("-r", "--race", type=int, default=0,
                        help="display race name corresponding to index number")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    actions = {
        "standings": print_standings,
        "race": print_race
    }

    for key, function in actions.items():
        if getattr(args, key):
            function(args)

if __name__ == "__main__":
    main()