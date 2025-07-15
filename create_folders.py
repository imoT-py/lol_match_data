import os

def folders():

    directory_path = 'E:\lol_data\\'

    ranks_all = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINUM", "EMERALD", "DIAMOND", "MASTER", "GRANDMASTER", "CHALLENGER"]

    for rank in ranks_all:
        specific_path = directory_path + rank
        try:
            os.mkdir(specific_path)
            print(f"Directory '{specific_path}' created successfully.")
        except FileExistsError:
            print(f"Directory '{specific_path}' already exists.")
        except PermissionError:
            print(f"Permission denied: Unable to create '{specific_path}'.")
        except Exception as e:
            print(f"An error occured: {e}")