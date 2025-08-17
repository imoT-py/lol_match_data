import requests
from api import headers
import time
from http.client import IncompleteRead
from requests.exceptions import ChunkedEncodingError, ConnectionError, HTTPError
from responses import response_match

def patch_info(match_ID):

  response = response_match(match_ID)


  data = response.json()
  patch_info = data['info']['gameVersion']

  time.sleep(2)
  return patch_info

