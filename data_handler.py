import numpy as np 
import pandas as pd 
import pickle

def map_input(altitude, origin, process):
	columns = pd.read_csv('./data/coffee_final.csv').drop(['Review'], axis = 1).columns
	features = np.zeros(len(columns))
	features[0] = altitude
	for i in range(len(columns)):
		if origin == columns[i]:
			features[i] = 1
		if process == columns[i]:
			features[i] = 1
	return features
