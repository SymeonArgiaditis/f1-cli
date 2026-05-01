def show_standings(drivers) -> None:
    for driver in drivers:
        print(f"{driver['position']}. {driver['Driver']['givenName']} {driver['Driver']['familyName']} - {driver['points']} pts ({driver['Constructors'][0]['name']})")

def show_race_info(race) -> None:
    name = race["raceName"]
    circuit = race["Circuit"]
    loc = circuit["Location"]
    
    print(f"====== {name} ======\n"
          f"Location: {circuit['circuitName']} - {loc['locality']}, {loc['country']}\n"
          f"Date: {race['date']}\n"
          f"Wiki: {circuit['url']}\n"
          )
    