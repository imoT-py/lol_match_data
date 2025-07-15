import os
from pathlib import Path

def folders():

    directory_path = Path(__file__).resolve().parent
    data_path = directory_path / 'outputs'

    ranks_all = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINUM", "EMERALD", "DIAMOND", "MASTER", "GRANDMASTER", "CHALLENGER"]
'''
    for rank in ranks_all:
        specific_path = str(data_path) + "/" + rank
        try:
            os.mkdir(data_path)
            os.mkdir(specific_path)
            print(f"Directory '{specific_path}' created successfully.")
        except FileExistsError:
            print(f"Directory '{specific_path}' already exists.")
        except PermissionError:
            print(f"Permission denied: Unable to create '{specific_path}'.")
        except Exception as e:
            print(f"An error occured: {e}")
'''