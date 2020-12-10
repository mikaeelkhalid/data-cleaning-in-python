corpus = 'i like this table in my room'
words = corpus.split(' ')

from nltk import pos_tag
tags = pos_tag(words)

for i in range(0, len(tags)):
    if tags[i][1] == 'DT':
        print(tags[i])