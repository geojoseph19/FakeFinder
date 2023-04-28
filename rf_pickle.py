import pandas as pd 
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import pickle
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier



git_link = 'https://github.com/geojoseph19/FakeFinder/raw/master/Datasets/Combined/insta_dataset.csv'
dataset = pd.read_csv(git_link)

x = dataset.drop("fake",axis=1)
#print(x.head(5))
y = dataset["fake"]
#print(y.head(5))

X_train, X_test, y_train, y_test =train_test_split(x, y, test_size=0.30, random_state=42)
rf_classifier = RandomForestClassifier(n_estimators = 20, criterion = 'entropy', random_state = 51)
rf_classifier.fit(X_train, y_train)

# Save the trained model to a file using pickle
with open('rf_classifier.pkl', 'wb') as f:
    pickle.dump(rf_classifier, f)





