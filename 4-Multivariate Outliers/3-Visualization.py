import pandas as pd
corpus = pd.read_csv('Dataset.csv')
print(corpus)

data = corpus.iloc[:, [2, 3]].values

import matplotlib.pyplot as plt
plt.scatter(data[:, 0], data[:, 1], s = 50, c = 'blue', marker = 'o')
plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.show()