from typing import Any

def show_standings(drivers: list[dict[str, Any]]) -> None:
    for driver in drivers:
        print(
            f"{driver['position']}. "
            f"{driver['Driver']['givenName']} "
            f"{driver['Driver']['familyName']} - "
            f"{driver['points']} pts "
            f"({driver['Constructors'][0]['name']})"
        )


def show_race_info(race: dict[str, Any]) -> None:
    name: str = race["raceName"]
    circuit: dict[str, Any] = race["Circuit"]
    loc: dict[str, Any] = circuit["Location"]
    
    print(
        f"====== {name} ======\n"
        f"Location: {circuit['circuitName']} - "
        f"{loc['locality']}, {loc['country']}\n"
        f"Date: {race['date']}\n"
        f"Wiki: {circuit['url']}\n"
    )
