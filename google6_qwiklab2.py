#! /usr/bin/env python3

import os
import requests
import json

#list all .txt files /data/feedback
#use os.listdir()
#traverse over each file from folder and take text from .txt files and create a dictionary with title, name, date and
#feedback

#use requests module to post dictionary to the website
#request.post() to http://104.198.165.1989/feedback
#run status code method

path = "/data/feedback/"
folders = os.listdir(path)
lista = []
dicta = {}
keys = ["title", "name", "date", "feedback"]
for file in folders:
  with open(path + file) as text_file:
    counter = 0
    for line in text_file.readlines():
      dicta[keys[counter]] = line.strip()
      counter += 1
    lista.append(dicta)
for l in lista:
  print(l)
  response = requests.post("http://104.198.165.189/feedback", data=l)
  #if not response.ok:
  #  raise Exception("Get failed with status code {}".format(response.status_code))
 # else:
    #print("Response status code: 201")
