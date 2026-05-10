#!/usr/bin/env python3

import sys

# Load the league list
league = set()
with open(sys.argv[1], 'r') as league_file:
    for line in league_file:
        league.add(int(line.strip()))

# Mapper function
for line in sys.stdin:
    # Parse input line
    page_id, popularity = line.strip().split('\t')
    page_id = int(page_id)
    popularity = int(popularity)

    # Calculate rank
    rank = sum(1 for page in league if page != page_id and page < page_id)

    # Emit key-value pair for the page's rank
    print('%s\t%s' % (rank, page_id))
