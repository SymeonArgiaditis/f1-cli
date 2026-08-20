import requests
from typing import Any

def safe_request(
        url: str, 
        timeout: float | tuple[float, float]=(10,20)
) -> requests.Response:
    try:
        response = requests.get(url, timeout=timeout)
        return response
    except requests.exceptions.ConnectionError:
        raise ConnectionError(
            "Error: could not connect to the F1 API. "
            "Check your internet connection."
        )

def get_standings() -> list[dict[str, Any]]:
    try:
        data: dict[str, Any] = safe_request(
            "https://api.jolpi.ca/ergast/f1/2026/driverstandings/"
        ).json()

        return data["MRData"]["StandingsTable"]["StandingsLists"][0][
            "DriverStandings"
        ]
    
    except KeyError:
        raise KeyError("Error: unexpected response from the F1 API.")

def get_race(choice: int) -> dict[str, Any]:
    try:
        data: dict[str, Any] = safe_request(
            "https://api.jolpi.ca/ergast/f1/2026/races/"
        ).json()

        races = data["MRData"]["RaceTable"]["Races"]

        if 1 <= choice <= len(races):
            return races[choice - 1]
        
        raise KeyError("Race not found.")
    
    except KeyError:
        raise KeyError("Error: unexpected response from the F1 API.")
