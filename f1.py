import requests
import json
import argparse

def get_standings() -> list: 
    response = requests.get("https://api.jolpi.ca/ergast/f1/2025/driverStandings/")
    data = response.json()
    drivers = data["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]

    return drivers

def print_standings(drivers) -> None:
    for driver in drivers:
        print(f"{driver["position"]}. {driver["Driver"]["givenName"]} {driver["Driver"]["familyName"]} - {driver["points"]} pts ({driver['Constructors'][0]['name']})")

parser = argparse.ArgumentParser(description="print F1 standings")

parser.add_argument("-s", "--standings", action="store_true",
                    help="display 2025 driver standings")

args = parser.parse_args()

if args.standings:
    print_standings(get_standings())
else:
    parser.print_help()