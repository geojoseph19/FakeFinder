def rf_model(data):
    import pandas as pd
    import pickle

    data = [data]

    # Load the saved model from file
    with open('rf_classifier.pkl', 'rb') as f:
        rf_classifier = pickle.load(f)


    # Load the new data for prediction
    datacsv = pd.DataFrame( data , columns = ['profile pic', 'nums/length username','fullname words','nums/length fullname','name==username','description length',
                                    'external URL','private','#posts','#followers','#follows'])

    # Make predictions using the loaded model
    prediction = rf_classifier.predict(datacsv)

    print(prediction)
    return prediction


