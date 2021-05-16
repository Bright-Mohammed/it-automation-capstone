#!/usr/bin/env python3

import json
import os
import requests

bname = "/data/feedback"
feedbk = []
for file in os.listdir(bname):
  filename = os.path.join(bname, file)
  with open(filename, 'r') as f:
    title = f.readline().strip()
    name = f.readline().strip()
    date = f.readline().strip()
    feedback = f.readline().strip()
    response = requests.post("http://35.184.17.201/feedback/", json={'title': title,
                             'name': name, 'date': date, 'feedback': feedback})
    print(response.status_code)
