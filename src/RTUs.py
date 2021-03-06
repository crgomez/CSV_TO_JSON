#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Maintainer: 'Carlos R Gomez <crgomez167@gmail.com>'

import csv
import json

# Read the CSV and add the data to a dictionary...
csvfile = open('plain_rtus.csv', 'r')
jsonfile = open('RTUs.json', 'w')

fieldnames = ("is_negated", "is_regex", "replace_target", "rule_id", "target", "target_match")

# Write data to a JSON file...
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile, indent=4)
    jsonfile.write('\n')
