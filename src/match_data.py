import requests
from api import headers
import time

def is_ranked(match_ID):
  
  while True:
    try:
      response = requests.get(f"https://europe.api.riotgames.com/lol/match/v5/matches/{match_ID}", headers=headers) # 2000 requests every 10 seconds
      print("match data", response.status_code)

      if response.status_code == 429:
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
  ranked_info = data['info']['queueId']
  time.sleep(2)
  return ranked_info
