#!/usr/bin/env python3

import re
import operator
import csv

per_user = {}
error = {}

def extract_username(log_line): 
    regex = r"\((\w+\.?\w+?)\)$"
    result = re.search(regex, log_line)
    return result.group(1)

def extract_error_name(log_line):
    regex = r"([A-Z]{5} )([\w+\s\']*) \((\w+\.?\w+?)\)"
    result = re.search(regex, log_line)
    return result.group(2)

filename = "syslog.log"

#1. Open a sylog file and append dictionaries values, searches based on regex from functions
with open(filename) as log:
    for log_line in log.readlines():
        log_line = log_line.strip()
        # Extract username
        username = extract_username(log_line)
        #Check if log consists of ERROR
        if "ERROR" in log_line:
            #Get ERROR name
            error_type = extract_error_name(log_line) 
            #Append error dictionary
            if  error_type not in error:
                error[error_type] = 1
            else:
                error[error_type] += 1
            #Append per_user dictionary
            if username not in per_user:
                per_user[username] = {"INFO": 0, "ERROR": 1} 
            else:
                per_user[username]["ERROR"] += 1
        #Check if log consists of INFO
        elif "INFO" in log_line:
            #Append per_user dictionary if user doesn't exist
            if username not in per_user:
                per_user[username] = {"INFO": 1, "ERROR": 0}
            else:
                per_user[username]["INFO"] += 1

#2. Create CSV files report from error dictionary
with open("error_message.csv", 'w+') as error_file:
    error_dict = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
    writer = csv.writer(error_file)
    writer.writerow(["Error", "Count"])
    writer.writerows(error_dict)

#3. Create CSV files report from user_statistics dictionary
with open("user_statistics.csv", "w+") as user_list:
    per_user_dict = dict(sorted(per_user.items(), key=operator.itemgetter(0)))
    user_list.write("Usernames,INFO,ERROR"+"\n")
    for k in per_user_dict:
        user_list.write("{},{},{}\n".format(k, per_user[k]["INFO"], per_user[k]["ERROR"]))