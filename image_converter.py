#!/usr/bin/env python3

from PIL import Image
import os

bas = "./images"

new_size = (128, 128)
for root, dir, files in os.walk(bas):
  for img in files:
    outfile = img[:-3] + ".jpeg"
    #print (outfile)
    im = Image.open(os.path.join(bas, img)).convert('RGB')
    im.rotate(90).resize(new_size).save(os.path.join("/opt/icons/", outfile), "JPEG", quality=90)