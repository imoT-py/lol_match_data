import requests
from api import headers
import time
from http.client import IncompleteRead
from requests.exceptions import ChunkedEncodingError, ConnectionError, HTTPError
from pathlib import Path
from responses import response_user

def user_rank():
    
    directory_path = Path(__file__).resolve().parent.parent
    data_path = directory_path / 'outputs'
    
    with open(str(data_path) + "/" + "users.txt", "r") as file:
        for line in file:
            user = line.strip()

            response = response_user(user)

            data = response.json()

            if data: 
                try:
                    rank = data[0]['tier']
                    tier = data[0]['rank']
                    
                    with open(str(data_path) + "/" + "users_with_rank.txt", "a") as file:
                        file.write(user + ' ' + rank + ' ' + tier + '\n')
                except KeyError:
                    print("Error: ")
                    print(data)
            else:
                with open(str(data_path) + "/" + "users_with_rank.txt", "a") as file:
                    file.write(user + ' ' + 'unranked' + ' ' + 'unranked' + '\n')