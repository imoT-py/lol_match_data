from matches import matches
from match_data import is_ranked
from match_timeline import timeline

def process(puuids, number_count, rank):

    for user_id in puuids:
        match_ids = matches(user_id, number_count)

        for match in match_ids:
            ranked = is_ranked(match)
            
            if ranked == 420:
                timeline(match, rank)
                print("File saved!")
            else:
                pass