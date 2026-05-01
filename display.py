from api import get_standings, get_race

def run_standings(args) -> None:
    drivers = get_standings()
    for driver in drivers:
        print(f"{driver['position']}. {driver['Driver']['givenName']} {driver['Driver']['familyName']} - {driver['points']} pts ({driver['Constructors'][0]['name']})")

def run_race(args) -> None:
    print(get_race(args.race))