from get_data.get_auth import get_auth_token
from get_data.get_long_fav_artists import get_long_fav_artists
from get_data.get_med_fav_artists import get_med_fav_artists
from get_data.get_short_fav_artists import get_short_fav_artists

from data_processing.generate_ratings import get_ratings_df
from data_processing.get_similarity import get_similarity_rating

# ic2uyujb93pc2hj6hpfibmnkp
# 1224546500

def run_get_ratings(username):
    # get auth token for username
    token = get_auth_token(username=username)
    
    # get artist from all time frames
    if token:
        top_artists = {
                        'long' : get_long_fav_artists(token),  
                        'medium' : get_med_fav_artists(token), 
                        'short' : get_short_fav_artists(token)
                    }
    else:
        print('Error, cannot get authorization token')

    import pandas as pd

    # get ratings df and sort it by ratings in ascending order
    ratings_df_sorted = get_ratings_df(top_artists).sort_values(by='rating', ascending=False)

    # return ratings df as a json so it can be sent from flask server to react
    return ratings_df_sorted.to_json(orient='columns')
