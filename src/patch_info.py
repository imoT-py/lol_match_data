import requests
from api import headers
import time

def patch_info(match_ID):

  while True:
    response = requests.get(f"https://europe.api.riotgames.com/lol/match/v5/matches/{match_ID}", headers=headers) # 2000 requests every 10 seconds
    if response.status_code == 200:
      break
    else:
      print(">>>Waiting for API")
      time.sleep(60)
      continue

  data = response.json()
  patch_info = data['info']['gameVersion']

  time.sleep(5)
  return patch_info

