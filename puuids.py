import requests
from api import headers
import time

def get_puuids():

    ranks = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINUM", "EMERALD", "DIAMOND"]
    tiers = ["I", "II", "III", "IV"]
    list_puuids = []

    for rank in ranks:
        for tier in tiers:
            # Inqure specific user list segment 
            for page in range(1, 51):

                while True:
                    response = requests.get(f"https://euw1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/{rank}/{tier}?page={page}", headers=headers) # 50 requests every 10 seconds
                    if response.status_code == 200:
                        break
                    else:
                        print("Waiting for API")
                        time.sleep(20)
                        continue

                data = response.json()
                # Get user IDs
                for user in data:
                    inner_data = user['puuid']
                    list_puuids.append(inner_data)
        
            return list_puuids, rank
        

def get_puuids_challengers():       
    response = requests.get("https://euw1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5", headers=headers)
    data = response.json()
    challengers = data['entries']

    list_puuids = []

    for challenger in challengers:
        puuid_data = challenger['puuid']
        list_puuids.append(puuid_data)
    
    return list_puuids


def get_puuids_grandmasters():       
    response = requests.get("https://euw1.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5", headers=headers)
    data = response.json()
    grandmasters = data['entries']

    list_puuids = []

    for grandmaster in grandmasters:
        puuid_data = grandmaster['puuid']
        list_puuids.append(puuid_data)
    
    return list_puuids



def get_puuids_masters():       
    response = requests.get("https://euw1.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5", headers=headers)
    data = response.json()
    masters = data['entries']

    list_puuids = []

    for master in masters:
        puuid_data = master['puuid']
        list_puuids.append(puuid_data)
    
    return list_puuids