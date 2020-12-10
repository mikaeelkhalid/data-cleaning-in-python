import pandas as pd
corpus = pd.read_csv('Dataset.csv')
print(corpus)

#Get features for scaling 
features = corpus.iloc[:, [2, 3, 4, 5]].values

#Manually handling missing value
features[0][2] = 0
print('\nFeatures\n')
print(features)

#normalize features using Robust Scaler
from sklearn.preprocessing import RobustScaler
rs = RobustScaler()
normalized_features = rs.fit_transform(features)

print('\nRobust Scaler Features\n')
import numpy as np
np.set_printoptions(suppress = True)
print(normalized_features)