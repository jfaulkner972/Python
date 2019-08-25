#!/usr/bin/python3
import datetime
import json

def keyword_bool_switch(keyword):
    keyword_dictionary = {"Failed password":True, "Invalid user":True }
    return keyword_dictionary.get(keyword, False)

def user_index_switch(keyword):
    user_index_dictionary = {"Failed password":8, "Invalid user":7 }
    return user_index_dictionary.get(keyword, False)

def parse_ip(log_file,date):
    parsed_errors = {}
    counter = 0
    for line in log_file:
        separated_line = line.split(" ")
        log_date = separated_line[0] + " " + separated_line[1]
        #if log_date == date:
        status_code = separated_line[5] + " " + separated_line[6]
        chosen_keyword = keyword_bool_switch(status_code)
        if chosen_keyword:
            dash_ip = separated_line[3]
            separated_ip = dash_ip.split("-")
            failed_ip = separated_ip[1] + "." + separated_ip[2] + "." + separated_ip[3] + "." + separated_ip[4]
            parsed_errors[counter] = [failed_ip, status_code, separated_line[user_index_switch(status_code)]]
            counter += 1

    return parsed_errors

currentDate = datetime.datetime.now().strftime("%b %d")
authLog = open("/var/log/secure","r")
print(json.dumps(parse_ip(authLog,currentDate)))
authLog.close()
