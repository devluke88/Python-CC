#! /usr/bin/env python3

import os
import requests

#list all .txt files /data/feedback, use os.listdir()
path = "/data/feedback/"
folders = os.listdir(path)

#traverse over each file from folder and take text from .txt files and create a dictionary with title, name, date and feedback
dicta = {}
keys = ["title", "name", "date", "feedback"]
for file in folders:
  with open(path + file) as text_file:
    counter = 0
    for line in text_file.readlines():
      dicta[keys[counter]] = line.strip()
      counter += 1 

    #use requests module to post dictionary to the website
    #request.post() to http://<corpweb-external-IP>/feedback/
    response = requests.post("http://34.69.68.154/feedback/", data=dicta)

    #run status code method
    if not response.ok:
      raise Exception("Get failed with status code {}".format(response.status_code))
    else:
      print("Response status code: 201")