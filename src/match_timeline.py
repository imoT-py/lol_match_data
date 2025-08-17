import requests
from patch_info import patch_info
from api import headers
import time
from pathlib import Path
from match_and_user_info import match_and_user_info
from http.client import IncompleteRead
from requests.exceptions import ChunkedEncodingError, ConnectionError, HTTPError
from responses import response_match
from responses import response_timeline

def timeline(match_ID, rank):

    frame_num = 0

    # timeline of a specific match
    
    response = response_timeline(match_ID)
    response_info = response_match(match_ID)



    time.sleep(2)        
    data = response.json()
    data_match_user_info = response_info.json()

    # get the list of frames
    outer_data = data['info']['frames']
    # get the list of participants
    participants = data['info']['participants']
    # get actual patch number
    #patch_data = patch_info(match_ID)

    directory_path = Path(__file__).resolve().parent.parent
    data_path = directory_path / 'outputs'

    # loop through every frame
    for frame in outer_data:
        frame_num += 1
        for i in range(1, 11):
            inner_data = frame['participantFrames'][str(i)]
            # First columns always be match_ID ,second frame number, third puuid, fourth patch number 
            with open(str(data_path) + "/" + rank.upper() + "/" + match_ID + ".txt", "a+") as f:
                print(match_ID, end=" ", file=f)
                print(frame_num, end=" ", file=f)
                print(participants[i-1]['puuid'], end=" ", file=f)
                #print(patch_data, end=" ", file=f)
            
                # Get teamId, lane, championName, win or lose
                user_info = match_and_user_info(data_match_user_info, participants[i-1]['puuid'])
                for info in user_info:
                    print(str(info), end=" ", file=f)

            # Get user_list to a different file '''
            with open(str(data_path) + "/" + "users.txt", "r") as users_file:
                existing_users = set(users_file.read().splitlines())
            if participants[i-1]['puuid'] not in existing_users:
                    with open(str(data_path) + "/" + "users.txt", "a") as users_file:
                        users_file.write(participants[i-1]['puuid'] + '\n')

            # loop through every user and get their stats
            for key, value in inner_data.items():
                if key == 'championStats' or key == 'damageStats' or key == 'position':
                    for key, value in value.items():
                        with open(str(data_path) + "/" + rank.upper() + "/" + match_ID + ".txt", "a") as f:
                            print(value, end=" ", file=f)
                else:
                    with open(str(data_path) + "/" + rank.upper() + "/" + match_ID + ".txt", "a") as f:
                        print(value, end=" ", file=f)
            with open(str(data_path) + "/" + rank.upper() + "/" + match_ID + ".txt", "a") as f:            
                print(file=f)
        #with open(str(data_path) + "/" + rank.upper() + "/" + match_ID + ".txt", "a") as f:            
        #        print(file=f)