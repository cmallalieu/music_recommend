import numpy as np
import pandas as pd

def get_similarity_rating(ratings_df):
    
    # get number of rows
    half_rows = ratings_df['artistName'].count() / 2

    # split into 2 dfs
    df1, df2 = np.split(ratings_df, [int(half_rows)], axis=0)

    # create ndarray of all unique artists from both dfs
    full_unique = pd.Series.append(df1['artistName'], df2['artistName']).unique()

    # create dataframe with combined unique artists and frequencies with NaN values filled with 0
    test = pd.merge(df1, df2, on="artistName", how="outer")

    # Construct full dataset and convert catagorical artistName and artistId to numerical ids
    df_x = pd.DataFrame.from_dict({ 'userId' : [0 for i in range(test['artistName'].size)], 'artistId' : [i for i in range(test['artistName'].size)], 'rating' : test['rating_x']})
    df_y = pd.DataFrame.from_dict({ 'userId' : [1 for i in range(test['artistName'].size)], 'artistId' : [i for i in range(test['artistName'].size)], 'rating' : test['rating_y']})
    dataset = pd.DataFrame.append(df_x, df_y)

    # seperate dataset into dataframe with only NaN and no NaN
    dataset_no_zeros = dataset[dataset['rating'].notna()]
    dataset_zeros = dataset[dataset['rating'].isna()]

    # import data into suprise dataset
    from surprise import Reader, Dataset
    reader = Reader(rating_scale=(0, 1))
    data_no_zeros = Dataset.load_from_df(dataset_no_zeros[['userId', 'artistId', 'rating']], reader)

    # split dataset into train and test
    from surprise.model_selection import train_test_split
    trainset, testset = train_test_split(data_no_zeros, test_size=0.2)
    trainset = data_no_zeros.build_full_trainset()

    # fit SVD model
    from surprise import SVD, accuracy
    algo = SVD()
    algo.fit(trainset)

    # Make prediction
    predictions = algo.test(testset)

    # Test model accuracy use root mean squared error
    from surprise import accuracy
    accuracy.rmse(predictions)

    # Load in full data df into suprise dataset object
    data = Dataset.load_from_df(dataset[['userId', 'artistId', 'rating']], reader)

    # cast suprise dataset object into suprise trainset object
    data = data.build_full_trainset()

    # Get predictions for NaN values
    uids = [data.to_raw_uid(uid) for uid in dataset_zeros['userId']]
    iids = [data.to_raw_iid(iid) for iid in dataset_zeros['artistId']]
    r_ui =[r_ui for r_ui in dataset_zeros['rating']]
    predictions = [(uids[x], iids[x], algo.predict(uids[x], iids[x], r_ui[x], verbose=False)[3]) for x in range(len(dataset_zeros['userId']))]

    # merge NaN values in original dataset with predicted values
    predicted_df = pd.DataFrame(predictions, columns=['userId', 'artistId', 'rating'])
    final_vectors = pd.concat([dataset_no_zeros, predicted_df], ignore_index=True, sort=False)

    # seperate user listening vectors
    user_1_vector = final_vectors[final_vectors['userId'] == 0]['rating']
    user_2_vector = final_vectors[final_vectors['userId'] == 1]['rating']

    from scipy.spatial.distance import cosine

    user_similarity = cosine(user_1_vector, user_2_vector)

    return user_similarity

