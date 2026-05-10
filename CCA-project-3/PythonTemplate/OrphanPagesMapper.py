#!/usr/bin/env python3

import sys

# Mapper function
for line in sys.stdin:
    # Parse input line
    page_id, links = line.strip().split('\t', 1)
    links = set(map(int, links.split(',')))

    # Emit key-value pairs for linked pages
    for linked_page in links:
        print('%s\t%s' % (linked_page, page_id))

    # Emit key-value pair for the page itself
    print('%s\t%s' % (page_id, page_id))  # Emit the page itself to handle self-links
