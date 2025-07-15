import requests
from api import headers
import time

def user_rank():
    with open("E:\lol_data\\users.txt", 'r') as file:
        for line in file:
            user = line.strip()

            while True:
                response = requests.get(f"https://euw1.api.riotgames.com/lol/league/v4/entries/by-puuid/{user}", headers=headers) 
                if response.status_code == 200:
                    break
                else:
                    print("Waiting for API")
                    time.sleep(20)
                    continue

            data = response.json()

            if data: 
                try:
                    rank = data[0]['tier']
                    tier = data[0]['rank']
                    
                    with open("E:\lol_data\\users_with_rank.txt", "a") as file:
                        file.write(user + ' ' + rank + ' ' + tier + '\n')
                except KeyError:
                    print("Error: ")
                    print(data)
            else:
                with open("E:\lol_data\\users_with_rank.txt", "a") as file:
                    file.write(user + ' ' + 'unranked' + ' ' + 'unranked' + '\n')