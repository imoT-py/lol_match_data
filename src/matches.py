import requests
from api import headers
import time

def matches(user_id, match_count):
    
    list_matches = []

    while True:
        response = requests.get(f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{user_id}/ids?count={match_count}", headers=headers) # 2000 requests every 10 seconds
        if response.status_code == 200:
            break
        else:
            print("Waiting for API")
            time.sleep(20)
            continue
    
    
    matches = response.json()

    for match in matches:
        list_matches.append(match)

    return list_matches