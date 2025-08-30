from puuids import get_puuids_challengers
from puuids import get_puuids_grandmasters
from puuids import get_puuids_masters
from puuids import get_puuids
from process import process
from create_folders import folders
from user_rank import user_rank
import time

# Create folders based on ranks
folders()
'''
#Get the user_IDs in a list | Below DIAMOND
puuids, rank = get_puuids()
process(puuids, 30, rank)


#Get the Challengers
puuids = get_puuids_challengers()
process(puuids, 100, 'challenger')


#Get the Grandmasters
puuids = get_puuids_grandmasters()
process(puuids, 100, 'grandmaster')
'''
#Get the Masters
puuids = get_puuids_masters()
process(puuids, 100, 'master')

'''
#Create user_rank folder with all users and their ranks
user_rank()
'''