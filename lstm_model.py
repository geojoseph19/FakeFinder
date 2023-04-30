def lstm_model(data):
    import pandas as pd
    import numpy as np
    import pickle
    from keras.models import Sequential
    from keras.layers import LSTM, Dense
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler


    # Load the saved StandardScaler and LSTM model from disk
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)

    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    # Preprocess the input data using the saved StandardScaler
    input_data = pd.DataFrame(np.array(data).reshape(1,-1), columns=['profile pic', 'nums/length username', 'fullname words', 'nums/length fullname', 'name==username', 'description length', 'external URL', 'private', '#posts', '#followers', '#follows'])
    input_data_normalized = scaler.transform(input_data)

    # Make predictions using the saved LSTM model
    input_data_reshaped = np.reshape(input_data_normalized, (input_data_normalized.shape[0], input_data_normalized.shape[1], 1))
    y_pred = model.predict(input_data_reshaped)
    # print("Prediction:", y_pred)

    # Make binary predictions on new data
    binary_predictions = (y_pred >= 0.3).astype(int)

    binary_predictions = binary_predictions[0] # since op is [[x]]

    return binary_predictions