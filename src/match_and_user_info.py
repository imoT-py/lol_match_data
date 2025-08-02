import requests
from api import headers

def match_and_user_info(match_ID, user):

    response = requests.get(f"https://europe.api.riotgames.com/lol/match/v5/matches/{match_ID}", headers=headers) # 2000 requests every 10 seconds

    data = response.json()
    print("data", data)
    li = []

    for i in range(0, 10):
        puuid = data['info']['participants'][i]['puuid']
        if user == puuid:
            team_id = data['info']['participants'][i]['teamId']
            li.append(data['info']['participants'][i]['teamId'])
            li.append(data['info']['participants'][i]['lane'])
            li.append(data['info']['participants'][i]['championName'])
            li.append(data['info']['gameVersion'])

            for j in range(0, 2):
                team = data["info"]["teams"][j]['teamId']
                if team_id == team:
                    li.append(data["info"]["teams"][j]['win'])

    return li


