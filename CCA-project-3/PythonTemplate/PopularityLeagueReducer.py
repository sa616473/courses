#!/usr/bin/env python3

import sys

# Reducer function
current_rank = None
current_count = 0
for line in sys.stdin:
    # Parse input line
    rank, page_id = line.strip().split('\t')
    rank = int(rank)

    # Update count if same rank
    if current_rank == rank:
        current_count += 1
    else:
        # Output rank and count
        if current_rank is not None:
            print('%s\t%s' % (current_rank, current_count))
        current_rank = rank
        current_count = 1

# Output the last rank and count
if current_rank is not None:
    print('%s\t%s' % (current_rank, current_count))
