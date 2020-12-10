import pandas as pd
corpus = pd.read_csv('Dataset.csv').values

# raw data
print(corpus)

# detect missing values in the data
print('\nThe records with missing values...')
symbols = ['?', '*', '#', 'Nan']
for row in corpus:
    if set(row) & set(symbols):
        print(row)
        