import numpy as np 
import pandas as pd 
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix as cm
from sklearn.preprocessing import StandardScaler
import scipy
import pickle

class EnsembleClassifier(object):

	def __init__(self, data, clf):

		self.data = data
		self.X_data = None
		self.train_label = None
		self.test_label = None
		self.clf = clf


	def load_data(self):
		X = self.data.drop(['Review'], axis = 1)
		y = self.data.Review
		X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle = True)

		#scaler = StandardScaler()
		#scaler.fit(X_train)
		#X_train_scaled = scaler.transform(X_train)
		#X_test_scaled = scaler.transform(X_test)
		self.X_data	= [X_train, X_test]
		self.train_label = y_train
		self.test_label	= y_test

	def fit(self):
		self.load_data()
		self.clf.fit(self.X_data[0],self.train_label)
		return self.clf


	def predict(self):
		return self.clf.score(self.X_data[1], self.test_label)

	def save(self):
		model = self.fit()
		pickle.dump(model, open('model.pkl', 'wb'))

