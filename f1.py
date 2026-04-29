import requests
import argparse

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

#Argument Parser
parser = argparse.ArgumentParser(description="print F1 standings")

parser.add_argument("-s", "--standings", action="store_true",
                    help="display 2025 driver standings")
#choices=range(0,24)
parser.add_argument("-r", "--race", type=int, default=0,
                    help="display race name corresponding to number")

args = parser.parse_args()
choice = args.race

if args.standings:
    print_standings(get_standings())
if args.race:
    print_race(get_race(choice))