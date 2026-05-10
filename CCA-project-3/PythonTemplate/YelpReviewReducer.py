#!/usr/bin/env python3

import sys

# Reducer function
current_business_id = None
total_score = 0
total_length = 0
num_reviews = 0

for line in sys.stdin:
    business_id, stars, token = line.strip().split('\t')

    # Convert stars to adjusted score (-2 to 2)
    adjusted_stars = (int(stars) - 3) / 2

    # Accumulate score and length
    if current_business_id == business_id:
        total_score += adjusted_stars
        total_length += 1
    else:
        # Output average score for previous business_id
        if current_business_id:
            print('%s\t%s' % (current_business_id, total_score / total_length))
        current_business_id = business_id
        total_score = adjusted_stars
        total_length = 1

# Output average score for the last business_id
if current_business_id:
    print('%s\t%s' % (current_business_id, total_score / total_length))
