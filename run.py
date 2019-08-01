from get_data.get_auth import get_auth_token
from get_data.get_long_fav_artists import get_long_fav_artists
from get_data.get_med_fav_artists import get_med_fav_artists
from get_data.get_short_fav_artists import get_short_fav_artists

from data_processing.generate_ratings import get_ratings_df
from data_processing.get_similarity import get_similarity_rating

# get auth token for username
token = get_auth_token(username='ic2uyujb93pc2hj6hpfibmnkp')

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

ratings_df = get_ratings_df(top_artists)
print(ratings_df)
similarity = get_similarity_rating(ratings_df)
print(similarity)