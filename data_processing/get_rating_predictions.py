    
def get_rating_predictions(dataset_no_zeros, dataset_zeros, dataset):
    
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
    import pandas as pd
    data = Dataset.load_from_df(dataset[['userId', 'artistId', 'rating']], reader)

    # cast suprise dataset object into suprise trainset object
    data = data.build_full_trainset()

    # Get predictions for NaN values
    uids = [data.to_raw_uid(uid) for uid in dataset_zeros['userId']]
    iids = [data.to_raw_iid(iid) for iid in dataset_zeros['artistId']]
    r_ui =[r_ui for r_ui in dataset_zeros['rating']]
    predictions = [(uids[x], iids[x], algo.predict(uids[x], iids[x], r_ui[x], verbose=False)[3]) for x in range(len(dataset_zeros['userId']))]

    return predictions