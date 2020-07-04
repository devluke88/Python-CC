#This is qwiklab from Google Pyhon COurse on Coursera
#1. create first bash script so we create oldFiles.txt and look for a list in list.txt then take "jane" related files to append to oldFiles.txt
#!/bin/bash

> oldFiles.txt
files=$(grep ' jane ' ../data/list.txt | cut -d' ' -f 3)

for file in $files; do 
    if test -e ..$file; then echo "..$file" >> oldFiles.txt; fi
done

#2. Create python script which open file take line and replace the line then run subprocess.run() to change file names
#!/usr/bin/env python3

import sys
import subprocess

with open(sys.argv[1]) as file:
    for line in file.readlines():
        old_name = line.strip()
        new_name = line.strip().replace("jane", "jdoe")
        subprocess.run("mv " + old_name + " " + new_name, shell=True)