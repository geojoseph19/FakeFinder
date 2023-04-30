import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score

git_link = 'https://github.com/geojoseph19/FakeFinder/raw/master/Datasets/Combined/insta_dataset.csv'
data = pd.read_csv(git_link)

X = data.drop('fake', axis=1)
y = data['fake']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

with open('knn_model.pkl', 'wb') as f:
    pickle.dump(knn, f)