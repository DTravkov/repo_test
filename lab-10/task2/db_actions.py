from get_data import *
from fill_data import *

def player_in_db(name,db_names):
    return name in db_names

def get_player_score(name):
    for player in get_data():
        if player[0] == name:
            return player[1]

