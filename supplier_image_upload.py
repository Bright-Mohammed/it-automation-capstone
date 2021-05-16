#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
bas = "./supplier-data/images"
for img in os.listdir(bas):
  with open(os.path.join(bas, img), 'rb') as opened:
      r = requests.post(url, files={'file': opened})