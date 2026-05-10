#!/usr/bin/env python3
import sys

# Initialize variables
current_word = None
current_count = 0
word = None

# Reducer function
for line in sys.stdin:
    # Parse the input we got from mapper
    word, count = line.strip().split('\t', 1)

    # Convert count to int
    try:
        count = int(count)
    except ValueError:
        # Count was not a number, so ignore this line
        continue

    # Handle input validation
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Output word count pair
            print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

# Output the last word count pair
if current_word == word:
    print('%s\t%s' % (current_word, current_count))
