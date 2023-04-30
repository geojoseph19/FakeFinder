def knn_model(data):

    import pandas as pd
    import pickle
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsClassifier

    with open('knn_model.pkl', 'rb') as f:
        knn_loaded = pickle.load(f)
    
    data = [data]

    # create a dataframe with the input data and set the column names to match the training data
    new_data = pd.DataFrame(data, columns = ['profile pic', 'nums/length username','fullname words','nums/length fullname','name==username','description length',
                                             'external URL','private','#posts','#followers','#follows'])

    # make a prediction using the modified input data
    prediction = knn_loaded.predict(new_data)

    return prediction