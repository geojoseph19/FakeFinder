import pandas as pd
import numpy as np
import pickle
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load dataset
git_link = 'https://github.com/geojoseph19/FakeFinder/raw/master/Datasets/Combined/insta_dataset.csv'
df = pd.read_csv(git_link)

# Preprocess data
numerical_cols = ['profile pic', 'nums/length username', 'fullname words', 'nums/length fullname', 'name==username', 'description length', 'external URL', 'private', '#posts', '#followers', '#follows']
X = df[numerical_cols]
y = df['fake']

# Normalize numerical variables
scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)

# Save the StandardScaler to disk
with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size=0.2, random_state=40)

# Define LSTM model
model = Sequential()
model.add(LSTM(64, input_shape=(X_train.shape[1], 1)))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train LSTM model
X_train_reshaped = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
model.fit(X_train_reshaped, y_train, epochs=10, batch_size=32)

# Save the trained LSTM model to disk
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)