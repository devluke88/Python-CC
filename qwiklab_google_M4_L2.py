#!/usr/bin/env python3

import  subprocess
import os.path
from multiprocessing import Pool

# Run function to backup files:
def run(task):
    src = task
    dest = src.replace("../data/prod/", "../data/prod_backup/")
    subprocess.call(["rsync", "-arq", src, dest])

if __name__ == "__main__":
    path = "../data/prod/"
    # Create a list with paths:
    tasks = []
    # We iterate through path (all folders and files) with os.walk:
    for dirpath, dirnames, filenames in os.walk(path):
        for name in dirnames:
            src = os.path.join(dirpath, name)
            # Append path to list:
            tasks.append(src)
        for file in filenames:
            src = os.path.join(dirpath, file)
            # Append path to list:
            tasks.append(src)
    # Create a pool of specific nuber of CPUs:        
    p = Pool(len(tasks))
    # Start each task within the pool:
    p.map(run, tasks)    