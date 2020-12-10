import pandas as pd
corpus = pd.read_csv('Dataset.csv')
print(corpus)

data = corpus.iloc[: , 2 : 6].values

data[0][2] = 0  #hard coded imputation of missing value of payment in first record
print(data)

from sklearn.neighbors import LocalOutlierFactor

lof = LocalOutlierFactor(n_neighbors = 2)
print(lof)

result = lof.fit_predict(data)

print('\n Multivariate Outliers (Records) labeled with -1', result)