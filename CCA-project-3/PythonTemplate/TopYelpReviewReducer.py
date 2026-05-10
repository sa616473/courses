#!/usr/bin/env python3

import sys

# Reducer function
count = 0

for line in sys.stdin:
    average_score, business_id = line.strip().split('\t')

    # Output top 10 business_ids with highest average score
    if count < 10:
        print('%s\t%s' % (business_id, average_score))
        count += 1
