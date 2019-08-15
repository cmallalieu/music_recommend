import numpy as np
import pandas as pd
from data_processing.get_rating_predictions import get_rating_predictions

def get_similarity_rating(json_1, json_2):

    # convert users json into dataframes
    df1 = pd.read_json(orient='columns')
    df2 = pd.read_json(orient='columns')

    # create dataframe with combined unique artists and frequencies
    unique_merged = pd.merge(df1, df2, on="artistName", how="outer")

    # Construct full dataset and convert catagorical artistName and artistId to numerical ids
    df_x = pd.DataFrame.from_dict({ 'userId' : [0 for i in range(unique_merged['artistName'].size)],
            'artistId' : [i for i in range(unique_merged['artistName'].size)], 'rating' : unique_merged['rating_x']})
    df_y = pd.DataFrame.from_dict({ 'userId' : [1 for i in range(unique_merged['artistName'].size)],
            'artistId' : [i for i in range(unique_merged['artistName'].size)], 'rating' : unique_merged['rating_y']})
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

