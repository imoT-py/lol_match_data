import requests
from patch_info import patch_info
from api import headers
import time

def timeline(match_ID, rank):

    frame_num = 0

    # timeline of a specific match
    while True:
        response = requests.get(f"https://europe.api.riotgames.com/lol/match/v5/matches/{match_ID}/timeline", headers=headers)
        
        if response.status_code == 200:
            break
        else:
            print(">>>sleeping")
            time.sleep(20)
            print(">>>up again")
            continue

    data = response.json()

    # get the list of frames
    outer_data = data['info']['frames']
    # get the list of participants
    participants = data['info']['participants']
    # get actual patch number
    patch_data = patch_info(match_ID)

    # loop through every frame
    for frame in outer_data:
        frame_num += 1
        for i in range(1, 11):
            inner_data = frame['participantFrames'][str(i)]
            # First columns always be match_ID ,second frame number, third puuid, fourth patch number 
            with open(f"E:\lol_data\{rank}\{match_ID}.txt", "a") as f:
                print(match_ID, end=" ", file=f)
                print(frame_num, end=" ", file=f)
                print(participants[i-1]['puuid'], end=" ", file=f)
                print(patch_data, end=" ", file=f)
            # Get user_list to a different file
            with open("E:\lol_data\\users.txt", "r") as users_file:
                existing_users = set(users_file.read().splitlines())
            if participants[i-1]['puuid'] not in existing_users:
                    with open("E:\lol_data\\users.txt", "a") as users_file:
                        users_file.write(participants[i-1]['puuid'] + '\n')

            # loop through every user and get their stats
            for key, value in inner_data.items():
                if key == 'championStats' or key == 'damageStats' or key == 'position':
                    for key, value in value.items():
                        with open(f"E:\lol_data\{rank}\{match_ID}.txt", "a") as f:
                            print(value, end=" ", file=f)
                else:
                    with open(f"E:\lol_data\{rank}\{match_ID}.txt", "a") as f:
                        print(value, end=" ", file=f)
            with open(f"E:\lol_data\{rank}\{match_ID}.txt", "a") as f:            
                print(file=f)
        with open(f"E:\lol_data\{rank}\{match_ID}.txt", "a") as f:            
                print(file=f)