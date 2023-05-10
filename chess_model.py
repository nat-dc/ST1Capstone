import sklearn
from sklearn.utils import shuffle
from sklearn import datasets
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style
from sklearn import svm
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

# Load libraries
import numpy
from matplotlib import pyplot as plt
from pandas import read_csv
from pandas import set_option
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.exceptions import DataDimensionalityWarning
from sklearn import preprocessing
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Data file import
df = pd.read_csv("chess_games.csv")

# Attribute to be predicted
predict = "winner"

df = df.drop_duplicates(subset=df.columns.difference(['game_id']))

df = df.drop('game_id', axis=1)
df = df.drop('white_id', axis=1)
df = df.drop('black_id', axis=1)
df = df.drop('opening_fullname', axis=1)
df = df.drop('opening_code', axis=1)
df = df.drop('moves', axis=1) #moves are being removed as they will be different for every single game so cannot contribute to machine learning
df = df.drop('turns', axis=1)
df = df.drop('victory_status', axis=1)

for col in df:
  if df[col].dtype =='object' or df[col].dtype == 'bool':
    df[col]=OrdinalEncoder().fit_transform(df[col].values.reshape(-1,1))

class_label =df['winner']
df = df.drop(['winner'], axis =1)
df = (df-df.min())/(df.max()-df.min())
df['winner']=class_label

chess_data = df.copy()
le = preprocessing.LabelEncoder()
rated = le.fit_transform(list(chess_data["rated"]))
winner = le.fit_transform(list(chess_data["winner"])) #0 = black, 1=draw, 2=white
time_increment = le.fit_transform(list(chess_data["time_increment"]))
white_rating = le.fit_transform(list(chess_data["white_rating"]))
black_rating = le.fit_transform(list(chess_data["black_rating"]))
opening_moves = le.fit_transform(list(chess_data["opening_moves"])) #how many moves in the opening
opening_shortname = le.fit_transform(list(chess_data["opening_shortname"]))
opening_response = le.fit_transform(list(chess_data["opening_response"]))
opening_variation = le.fit_transform(list(chess_data["opening_variation"]))

x = list(zip(rated, time_increment, white_rating, black_rating, opening_moves, opening_shortname, opening_response, opening_variation))
y = list(winner)

num_folds = 5
seed = 7
scoring = 'accuracy'

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state=seed)

np.shape(x_train), np.shape(x_test)

#models = []
#models.append(('DT', DecisionTreeClassifier()))
#models.append(('NB', GaussianNB()))
#models.append(('SVM', SVC()))
#models.append(('GBM', GradientBoostingClassifier()))
#models.append(('RF', RandomForestClassifier()))
#dt = DecisionTreeClassifier()
#nb = GaussianNB
#sv = SVC()
gb = GradientBoostingClassifier()
#rf = RandomForestClassifier()

#results = []
#names=[]
#print("Performance on training set:")
#for name, model in models:
#  kfold = KFold(n_splits=num_folds,shuffle=True,random_state=seed)
#  cv_results = cross_val_score(model, x_train, y_train, cv=kfold, scoring='accuracy')
#  results.append(cv_results)
#  names.append(name)
#  msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
#  msg += '\n'
#  print(msg)

best_model = gb
best_model.fit(x_train, y_train)
y_pred = best_model.predict(x_test)
print("Best model accuracy on test set:", accuracy_score(y_test, y_pred))
