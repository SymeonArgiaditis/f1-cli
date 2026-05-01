import requests

def safe_request(url, timeout=(10,20)):
    try:
        response = requests.get(url, timeout=timeout)
        return response
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Error: could not connect to the F1 API. Check your internet connection.")

def get_standings() -> list:
    try:
        data = safe_request("https://api.jolpi.ca/ergast/f1/2026/driverstandings/").json()
        return data["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]
    except KeyError:
        raise KeyError("Error: unexpected response from the F1 API.")

def get_race(choice) -> str:
    try:
        data = safe_request("https://api.jolpi.ca/ergast/f1/2026/races/").json()
        races = data["MRData"]["RaceTable"]["Races"]

        if choice <= len(races) and choice >= 1:
            return races[choice-1]["raceName"]
        return "Race not found."
    
    except KeyError:
        raise KeyError("Error: unexpected response from the F1 API.")