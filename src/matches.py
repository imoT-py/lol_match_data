import requests
from api import headers
import time
from http.client import IncompleteRead
from requests.exceptions import ChunkedEncodingError, ConnectionError, HTTPError
from responses import response_matches

def matches(user_id, match_count):
    
    list_matches = []

    response = response_matches(user_id, match_count)
        
        
    matches = response.json()

    for match in matches:
        list_matches.append(match)
    time.sleep(2)
    return list_matches
