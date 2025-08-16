import requests
from api import headers
import time

def matches(user_id, match_count):
    
    list_matches = []

    while True:
        try:
            response = requests.get(f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{user_id}/ids?count={match_count}", headers=headers) # 2000 requests every 10 seconds
            print("matches", response.status_code)
        
            if response.status_code == 429 or response.status_code == 503 or response.status_code == 504:
                print("Waiting for the API")
                time.sleep(30)
                continue
            
            break

        except (IncompleteRead, ChunkedEncodingError, ConnectionError) as e:
            print('IncompleteRead, ChunkedEncodingError, ConnectionError')
            print(e)
            time.sleep(2)                

        except HTTPError as e:
            print("HTTTPError", e)
            break
        
        except Exception as e:
            print("Exception", e)
            break
        
        
    matches = response.json()

    for match in matches:
        list_matches.append(match)
    time.sleep(2)
    return list_matches
