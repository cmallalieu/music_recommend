import numpy as np
from ordered_set import OrderedSet

    
def get_ratings_df(raw_fav_artist_data):    

    # sperate raw data into ordered sets
    raw_long = OrderedSet(raw_fav_artist_data['long'])
    raw_med = OrderedSet(raw_fav_artist_data['medium'])
    raw_short = OrderedSet(raw_fav_artist_data['short'])


    # generate 7 unique sets
    long_med_short = raw_long & raw_med & raw_short
    long_med = raw_long & raw_med - raw_short
    long_short = raw_long & raw_short - raw_med
    med_short = raw_med & raw_short - raw_long
    long = raw_long - raw_med - raw_short
    med = raw_med - raw_long - raw_short
    short = raw_short - raw_med - raw_long


    # get lengths for each set
    long_med_short_len = len(long_med_short)
    long_med_len = len(long_med)
    long_short_len = len(long_short)
    med_short_len = len(med_short)
    long_len = len(long)
    med_len = len(med)
    short_len = len(short)

    # generate raw int ratings of each artist with weight given to position in set
    ratings_long_med_short = np.array([(18 + long_med_short_len - i) for i in range(long_med_short_len)], dtype='int32')
    ratings_long_med = np.array([(12 + long_med_len - i) for i in range(long_med_len)], dtype='int32')
    ratings_long_short = np.array([(8 + long_short_len - i) for i in range(long_short_len)], dtype='int32')
    ratings_med_short = np.array([(5 + med_short_len - i) for i in range(med_short_len)], dtype='int32')
    ratings_long = np.array([(3 + long_len - i) for i in range(long_len)], dtype='int32')
    ratings_med = np.array([(2 + med_len - i) for i in range(med_len)], dtype='int32')
    ratings_short = np.array([(1 + short_len - i) for i in range(short_len)], dtype='int32')

    # append all ratings to a single np array and min max normalize them between [0, 1]
    from sklearn import preprocessing
    combined_ratings = np.concatenate((ratings_long_med_short, ratings_long_med, 
                                        ratings_long_short, ratings_med_short, ratings_long,
                                        ratings_med, ratings_short))

    min_max_scaler = preprocessing.MinMaxScaler()
    normalized_ratings = min_max_scaler.fit_transform(combined_ratings.reshape(-1, 1)).flatten()

    # append all names of artists to a single array to create a df
    combined_artists = np.concatenate((long_med_short, long_med, long_short, med_short, long, med, short))

    # create dataframe from ratings data
    import pandas as pd
    ratings_df = pd.DataFrame({'artistName' : combined_artists, 'rating' : normalized_ratings})
    
    return ratings_df

