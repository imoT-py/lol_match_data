import requests
from api import headers
import time
from http.client import IncompleteRead
from requests.exceptions import ChunkedEncodingError, ConnectionError, HTTPError

def get_puuids():

    ranks = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINUM", "EMERALD", "DIAMOND"]
    tiers = ["I", "II", "III", "IV"]
    list_puuids = []

    for rank in ranks:
        for tier in tiers:
            # Inqure specific user list segment 
            for page in range(1, 51):

                while True:
                    try:
                        response = requests.get(f"https://euw1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/{rank}/{tier}?page={page}", headers=headers) # 50 requests every 10 seconds
                        print(f"puuids, {rank}", response.status_code)

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
                # Get user IDs
                for user in data:
                    inner_data = user['puuid']
                    list_puuids.append(inner_data)
            time.sleep(2)
            return list_puuids, rank
        

def get_puuids_challengers():    
    while True:
        try:   
            response = requests.get("https://euw1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5", headers=headers)
            print("puuids chall", response.status_code)
            
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
    challengers = data['entries']

    list_puuids = []

    for challenger in challengers:
        puuid_data = challenger['puuid']
        list_puuids.append(puuid_data)
            
    return list_puuids


def get_puuids_grandmasters():  
    while True:
        try:       
            response = requests.get("https://euw1.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5", headers=headers)
            print("puuids grand_master", response.status_code)
        
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
    grandmasters = data['entries']

    list_puuids = []

    for grandmaster in grandmasters:
        puuid_data = grandmaster['puuid']
        list_puuids.append(puuid_data)
    
    return list_puuids



def get_puuids_masters():     
    while True:
        try:   
            response = requests.get("https://euw1.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5", headers=headers)
            print("puuids master", response.status_code)
            
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
    masters = data['entries']

    list_puuids = []

    for master in masters:
        puuid_data = master['puuid']
        list_puuids.append(puuid_data)
    
    return list_puuids
