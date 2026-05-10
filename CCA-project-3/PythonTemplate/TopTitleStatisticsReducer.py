#!/usr/bin/env python3

import sys
import math

# Initialize variables for statistics calculation
count = 0
sum_counts = 0
min_count = float('inf')
max_count = float('-inf')
squared_sum = 0

# Input comes from mapper.py
for line in sys.stdin:
    # Parse the input we got from mapper.py
    _, word_count = line.strip().split('\t')
    word_count = int(word_count)

    # Update statistics
    count += 1
    sum_counts += word_count
    min_count = min(min_count, word_count)
    max_count = max(max_count, word_count)
    squared_sum += word_count ** 2

# Calculate mean, variance (using formula: E[X^2] - E[X]^2), and floor all values to integers
mean = sum_counts // count
variance = (squared_sum // count) - (mean ** 2)

# Output statistics
print('Mean\t%d' % mean)
print('Sum\t%d' % sum_counts)
print('Minimum\t%d' % min_count)
print('Maximum\t%d' % max_count)
print('Variance\t%d' % variance)
