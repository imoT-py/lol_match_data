import requests
from api import headers
import time
from http.client import IncompleteRead
from requests.exceptions import ChunkedEncodingError, ConnectionError, HTTPError

def patch_info(match_ID):

  while True:
    response = requests.get(f"https://europe.api.riotgames.com/lol/match/v5/matches/{match_ID}", headers=headers) # 2000 requests every 10 seconds
    print("patch info", response.status_code)
    try:
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
  patch_info = data['info']['gameVersion']

  time.sleep(2)
  return patch_info

