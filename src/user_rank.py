import requests
from api import headers
import time
from http.client import IncompleteRead
from requests.exceptions import ChunkedEncodingError, ConnectionError, HTTPError
from pathlib import Path

def user_rank():
    
    directory_path = Path(__file__).resolve().parent.parent
    data_path = directory_path / 'outputs'
    
    with open(str(data_path) + "/" + "users.txt", "r") as file:
        for line in file:
            user = line.strip()

            while True:
                try:
                    response = requests.get(f"https://euw1.api.riotgames.com/lol/league/v4/entries/by-puuid/{user}", headers=headers) 
                    print("user", response.status_code)

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

            data = response.json()

            if data: 
                try:
                    rank = data[0]['tier']
                    tier = data[0]['rank']
                    
                    with open(str(data_path) + "/" + "users_with_rank.txt", "a") as file:
                        file.write(user + ' ' + rank + ' ' + tier + '\n')
                except KeyError:
                    print("Error: ")
                    print(data)
            else:
                with open(str(data_path) + "/" + "users_with_rank.txt", "a") as file:
                    file.write(user + ' ' + 'unranked' + ' ' + 'unranked' + '\n')