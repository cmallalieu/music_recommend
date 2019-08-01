import numpy as np
import pandas as pd
from data_processing.get_rating_predictions import get_rating_predictions

def get_similarity_rating(ratings_df):
    
    # get number of rows
    half_rows = ratings_df['artistName'].count() / 2

    # split into 2 dfs
    df1, df2 = np.split(ratings_df, [int(half_rows)], axis=0)

    # create dataframe with combined unique artists and frequencies with NaN values filled with 0
    test = pd.merge(df1, df2, on="artistName", how="outer")

    # Construct full dataset and convert catagorical artistName and artistId to numerical ids
    df_x = pd.DataFrame.from_dict({ 'userId' : [0 for i in range(test['artistName'].size)], 'artistId' : [i for i in range(test['artistName'].size)], 'rating' : test['rating_x']})
    df_y = pd.DataFrame.from_dict({ 'userId' : [1 for i in range(test['artistName'].size)], 'artistId' : [i for i in range(test['artistName'].size)], 'rating' : test['rating_y']})
    dataset = pd.DataFrame.append(df_x, df_y)

    # seperate dataset into dataframe with only NaN and no NaN
    dataset_no_zeros = dataset[dataset['rating'].notna()]
    dataset_zeros = dataset[dataset['rating'].isna()]

    # get list of predictions
    predictions = get_rating_predictions(dataset_no_zeros, dataset_zeros, dataset)

    # merge NaN values in original dataset with predicted values
    predicted_df = pd.DataFrame(predictions, columns=['userId', 'artistId', 'rating'])
    final_vectors = pd.concat([dataset_no_zeros, predicted_df], ignore_index=True, sort=False)

    # seperate user listening vectors
    user_1_vector = final_vectors[final_vectors['userId'] == 0]['rating']
    user_2_vector = final_vectors[final_vectors['userId'] == 1]['rating']

    from scipy.spatial.distance import cosine

    user_similarity = cosine(user_1_vector, user_2_vector)

    return user_similarity

