import pandas as pd
corpus = pd.read_csv('Dataset.csv')
print(corpus)

#Get features for scaling with normalization or min-max scaler
features = corpus.iloc[:, [2, 3, 4, 5]].values

#Manually handling missing value
features[0][2] = 0
print('\nFeatures\n')
print(features)

#normalize features using minmaxscaler
from sklearn.preprocessing import MinMaxScaler
mms = MinMaxScaler()
normalized_features = mms.fit_transform(features)

print('\nNormalized Features\n')
import numpy as np
np.set_printoptions(suppress = True)
print(normalized_features)