#!/usr/bin/env python
""" mapper.py """

import sys
k = 4 - 2

# input comes from STDIN (standard input)
for line in sys.stdin:
  # remove leading and trailing whitespace
  line = line.strip()
  
  n = len(line)
  for i in range(0, n - k):

    # write the results to STDOUT (standard output);
    # what we output here will be the input for the
    # Reduce step, i.e. the input for reducer.py
    #
    # tab-delimited; the trivial word count is 1
    print ('%s %s' % (line[i: i + k + 1], 1))