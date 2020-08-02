#!/usr/bin/env python3
#Google COursera - module 6, project 1 - you must be inside images folder, then run the following script to convert tiff images files from images folder and save it to /opt/icons folder

import glob
import os, sys
from PIL import Image

dest = os.path.join(os.getcwd(), "/opt/icons/")
#print(dest)

for infile in glob.glob("*"):
  f, e = os.path.splitext(infile)
  outfile = f
  # print("Plik outfile: {}".format(outfile))
  try:
    im = Image.open(infile).convert('RGB')
    im.rotate(-90)
    im.thumbnail((128,128))
    final_path = dest + outfile
    # print(final_path)
    im.save(final_path, "JPEG")
  except OSError as e:
    print("cannot convert because {}".format(e))