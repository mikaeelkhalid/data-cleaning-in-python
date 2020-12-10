import pandas as pd
corpus = pd.read_csv('Dataset.csv').values

# raw data
print(corpus)

# detect missing values in the data

#Handle the missing values (Deletion Strategy)
complete_data = []
symbols = ['?', '*', '#', 'Nan']
print('\nDeleted Records')
for row in corpus:
    if set(row) & set(symbols):
        print(row)
    else:
        complete_data.append(row)         #Keeping on the records without missing values (others deleted)
        
#Data after the deletion strategy applied on missing values
print('\n Complete Data (After Deletion)\n', complete_data)