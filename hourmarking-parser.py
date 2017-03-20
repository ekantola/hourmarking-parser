#! /usr/bin/python3

from __future__ import print_function  # also works with Python 2

import collections
import re
import sys

hour_items = collections.defaultdict(lambda: 0)

for line in sys.stdin:
    hours_hms, comment = line.split('\t', 1)
    hours_s, mins_s, secs_s = hours_hms.split(':', 2)
    hours = float(hours_s) + float(mins_s)/60

    labels = re.split('[,;]', comment)
    for label in labels:
        hour_items[label.strip().capitalize()] += hours / len(labels)

for label in hour_items.keys():
    print(str(round(hour_items[label], 2)) + '\t' + label)
