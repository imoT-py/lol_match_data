import requests
from api import headers

def match_and_user_info(data_match_info, user):

    data = data_match_info
    #print("data", data)
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

    print(li)                
    return li


