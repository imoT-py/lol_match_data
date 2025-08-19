import requests
from api import headers
import time
from http.client import IncompleteRead
from requests.exceptions import ChunkedEncodingError, ConnectionError, HTTPError

def response_match(match_ID):
    
    while True:
        try:
            response = requests.get(f"https://europe.api.riotgames.com/lol/match/v5/matches/{match_ID}", headers=headers) # 2000 requests every 10 seconds
            print("match data", response.status_code)

            if response.status_code in {429, 500, 502, 503, 504}:
                print("Waiting for the API")
                time.sleep(30)
                continue
                
            return response

        except (IncompleteRead, ChunkedEncodingError, ConnectionError) as e:
            print('IncompleteRead, ChunkedEncodingError, ConnectionError')
            print(e)
            print("IncompleteRead")
            time.sleep(30)
            continue               

        except HTTPError as e:
            print("HTTTPError", e)
            time.sleep(30)
            continue
            
        except Exception as e:
            print("Exception", e)
            time.sleep(30)
            continue
        
        
def response_timeline(match_ID):      
    
    while True:
        try:
            response = requests.get(f"https://europe.api.riotgames.com/lol/match/v5/matches/{match_ID}/timeline", headers=headers)
            print("timeline", response.status_code)
            
            if response.status_code in {429, 500, 502, 503, 504}:
                print("Waiting for the API")
                time.sleep(30)
                continue
                
            return response

        except (IncompleteRead, ChunkedEncodingError, ConnectionError) as e:
            print('IncompleteRead, ChunkedEncodingError, ConnectionError')
            print(e)
            print("IncompleteRead")
            time.sleep(30)
            continue                

        except HTTPError as e:
            print("HTTTPError", e)
            time.sleep(30)
            continue
            
        except Exception as e:
            print("Exception", e)
            time.sleep(30)
            continue
        
        
def response_puuids(rank, tier, page):      
      
    while True:
        try:
            response = requests.get(f"https://euw1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/{rank}/{tier}?page={page}", headers=headers) # 50 requests every 10 seconds
            print(f"puuids, {rank}", response.status_code)
            
            if response.status_code in {429, 500, 502, 503, 504}:
                print("Waiting for the API")
                time.sleep(30)
                continue
                
            return response

        except (IncompleteRead, ChunkedEncodingError, ConnectionError) as e:
            print('IncompleteRead, ChunkedEncodingError, ConnectionError')
            print(e)
            print("IncompleteRead")
            time.sleep(30)
            continue               

        except HTTPError as e:
            print("HTTTPError", e)
            time.sleep(30)
            continue
            
        except Exception as e:
            print("Exception", e)
            time.sleep(30)
            continue
        
        
def response_challengers():      
    
    while True:
        try:
            response = requests.get("https://euw1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5", headers=headers)
            print("puuids chall", response.status_code)
            
            if response.status_code in {429, 500, 502, 503, 504}:
                print("Waiting for the API")
                time.sleep(30)
                continue
                
            return response

        except (IncompleteRead, ChunkedEncodingError, ConnectionError) as e:
            print('IncompleteRead, ChunkedEncodingError, ConnectionError')
            print(e)
            print("IncompleteRead")
            time.sleep(30)
            continue                

        except HTTPError as e:
            print("HTTTPError", e)
            time.sleep(30)
            continue
            
        except Exception as e:
            print("Exception", e)
            time.sleep(30)
            continue                       
        

def response_grandmasters():      
    
    while True:
        try:
            response = requests.get("https://euw1.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5", headers=headers)
            print("puuids grand_master", response.status_code)
            
            if response.status_code in {429, 500, 502, 503, 504}:
                print("Waiting for the API")
                time.sleep(30)
                continue
                
            return response

        except (IncompleteRead, ChunkedEncodingError, ConnectionError) as e:
            print('IncompleteRead, ChunkedEncodingError, ConnectionError')
            print(e)
            print("IncompleteRead")
            time.sleep(30)
            continue                

        except HTTPError as e:
            print("HTTTPError", e)
            time.sleep(30)
            continue
            
        except Exception as e:
            print("Exception", e)
            time.sleep(30)
            continue  
        
        
def response_masters():      
    
    while True:
        try:
            response = requests.get("https://euw1.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5", headers=headers)
            print("puuids master", response.status_code)
            
            if response.status_code in {429, 500, 502, 503, 504}:
                print("Waiting for the API")
                time.sleep(30)
                continue
                
            return response

        except (IncompleteRead, ChunkedEncodingError, ConnectionError) as e:
            print('IncompleteRead, ChunkedEncodingError, ConnectionError')
            print(e)
            print("IncompleteRead")
            time.sleep(30)
            continue               

        except HTTPError as e:
            print("HTTTPError", e)
            time.sleep(30)
            continue
            
        except Exception as e:
            print("Exception", e)
            time.sleep(30)
            continue  
        

def response_matches(user_id, match_count):
    
    while True:
        try:
            response = requests.get(f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{user_id}/ids?count={match_count}", headers=headers) # 2000 requests every 10 seconds
            print("matches", response.status_code)

            if response.status_code in {429, 500, 502, 503, 504}:
                print("Waiting for the API")
                time.sleep(30)
                continue
                
            return response

        except (IncompleteRead, ChunkedEncodingError, ConnectionError) as e:
            print('IncompleteRead, ChunkedEncodingError, ConnectionError')
            print(e)
            print("IncompleteRead")
            time.sleep(30)
            continue                 

        except HTTPError as e:
            print("HTTTPError", e)
            time.sleep(30)
            continue
            
        except Exception as e:
            print("Exception", e)
            time.sleep(30)
            continue
        
        
def response_user(user):
    
    while True:
        try:
            response = requests.get(f"https://euw1.api.riotgames.com/lol/league/v4/entries/by-puuid/{user}", headers=headers) 
            print("user", response.status_code)

            if response.status_code in {429, 500, 502, 503, 504}:
                print("Waiting for the API")
                time.sleep(30)
                continue
                
            return response

        except (IncompleteRead, ChunkedEncodingError, ConnectionError) as e:
            print('IncompleteRead, ChunkedEncodingError, ConnectionError')
            print(e)
            print("IncompleteRead")
            time.sleep(30)
            continue                

        except HTTPError as e:
            print("HTTTPError", e)
            time.sleep(30)
            continue
            
        except Exception as e:
            print("Exception", e)
            time.sleep(30)
            continue       
        
        