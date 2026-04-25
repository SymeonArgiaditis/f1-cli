import requests
import json

def get_standings() -> list: 
    response = requests.get("https://api.jolpi.ca/ergast/f1/2025/driverStandings/")
    data = response.json()
    drivers = data["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]

    return drivers

def print_standings(drivers) -> None:
    for driver in drivers:
        print(f"{driver["position"]}. {driver["Driver"]["givenName"]} {driver["Driver"]["familyName"]} - {driver["points"]} pts ({driver['Constructors'][0]['name']})")

print_standings(get_standings())
