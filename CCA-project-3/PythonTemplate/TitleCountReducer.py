#!/usr/bin/env python3

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# Input comes from STDIN
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # Convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # Count was not a number, so silently
        # ignore/discard this line
        continue

    # Handle case when word is same as previous word
    if current_word == word:
        current_count += count
    else:
        # Emit result for previous word
        if current_word:
            print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

# Output the last word
if current_word == word:
    print('%s\t%s' % (current_word, current_count))
