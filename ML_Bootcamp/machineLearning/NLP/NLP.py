import nltk

# nltk.download_shell()

messages = [line.rstrip() for line in open('smsspamcollection/SMSSpamCollection')]

print(len(messages))

for mes_no, message in enumerate(messages[:10]):
    print(mes_no, message)
    print('\n')

# Detecing which one is spam which one is ham

import pandas as pd

messages = pd.read_csv('smsspamcollection/SMSSpamCollection', sep='\t', 
names=['label', 'message'])

print(messages.head())
