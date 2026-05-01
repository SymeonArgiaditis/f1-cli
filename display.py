from api import get_standings, get_race

def show_standings(drivers) -> None:
    for driver in drivers:
        print(f"{driver['position']}. {driver['Driver']['givenName']} {driver['Driver']['familyName']} - {driver['points']} pts ({driver['Constructors'][0]['name']})")

def show_race(race) -> None:
    print(race)