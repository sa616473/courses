#!/usr/bin/env python3

import sys
import json
import string

# Load stopwords
stopwords = set()
with open(sys.argv[1], 'r') as stopwords_file:
    for line in stopwords_file:
        stopwords.add(line.strip())

# Load delimiters
delimiters = set()
with open(sys.argv[2], 'r') as delimiters_file:
    for line in delimiters_file:
        delimiters.add(line.strip())

# Mapper function
for line in sys.stdin:
    review = json.loads(line)
    business_id = review["business_id"]
    stars = review["stars"]
    text = review["text"]

    # Tokenize review text
    tokens = [word.strip(string.punctuation).lower() for word in text.split() if word.strip(string.punctuation).lower() not in stopwords]

    # Emit business_id and adjusted stars
    for token in tokens:
        print('%s\t%s\t%s' % (business_id, stars, token))
