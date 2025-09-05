import requests
from api import headers
import time
from http.client import IncompleteRead
from requests.exceptions import ChunkedEncodingError, ConnectionError, HTTPError
from responses import response_puuids
from responses import response_challengers
from responses import response_grandmasters
from responses import response_masters

def get_puuids():

    ranks = ["BRONZE", "SILVER", "GOLD", "PLATINUM", "EMERALD", "DIAMOND"]
    tiers = ["I", "II", "III", "IV"]
    list_puuids = []

    for rank in ranks:
        for tier in tiers:
            # Inqure specific user list segment 
            for page in range(1, 51):

                response = response_puuids(rank, tier, page)

                data = response.json()
                # Get user IDs
                for user in data:
                    inner_data = user['puuid']
                    list_puuids.append(inner_data)
            time.sleep(2)
            
            print(len(list_puuids))
            return list_puuids, rank
        

def get_puuids_challengers():    
    
    response = response_challengers()
             
    data = response.json()
    challengers = data['entries']

    list_puuids = []

    for challenger in challengers:
        puuid_data = challenger['puuid']
        list_puuids.append(puuid_data)
            
    return list_puuids


def get_puuids_grandmasters():  
    
    response = response_grandmasters()
        
    data = response.json()
    grandmasters = data['entries']

    list_puuids = []

    for grandmaster in grandmasters:
        puuid_data = grandmaster['puuid']
        list_puuids.append(puuid_data)
    
    return list_puuids



def get_puuids_masters():     
    
    response = response_masters()
            
    data = response.json()
    masters = data['entries']

    list_puuids = []

    for master in masters:
        puuid_data = master['puuid']
        list_puuids.append(puuid_data)
    
    return list_puuids
