import requests
from responses import response_match
from api import headers
import time
from http.client import IncompleteRead
from requests.exceptions import ChunkedEncodingError, ConnectionError, HTTPError


def is_ranked(match_ID):
  
  response = response_match(match_ID)

  data = response.json()
  ranked_info = data['info']['queueId']
  time.sleep(2)
  return ranked_info
