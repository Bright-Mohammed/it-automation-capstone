#!/usr/bin/env python3

import json
import os
import requests

image_loc = "./supplier-data/images"
desc_loc = "./supplier-data/descriptions"
name = ""
weight = 0
description = ""
for file in os.listdir(desc_loc):
  d_filename = os.path.join(desc_loc, file)
  with open(d_filename, 'r') as f:
    name = f.readline().strip()
    weight = int(f.readline().strip(" lbs\n"))
    description = f.readline().strip()
    i_filename = os.path.join(desc_loc, file)
    response = requests.post("http://35.232.70.68/fruits/", json={'name': name,'weight': weight, 'description': description, 'image_name': file[0:3]+".jpeg"})