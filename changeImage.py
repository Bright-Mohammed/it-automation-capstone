#!/usr/bin/env python3

from PIL import Image
import os

bas = "./supplier-data/images"

new_size = (600, 400)
for img in os.listdir(bas):
  if img[-5:] == ".tiff":
    outfile = img[:-5] + ".jpeg"
    im = Image.open(os.path.join(bas, img)).convert('RGB')
    im.resize(new_size).save(os.path.join("./supplier-data/images", outfile), "JPEG", quality=90)