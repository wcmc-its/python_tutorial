#!/usr/bin/python

import requests
import re
import configparser
import sys
import argparse

parser = argparse.ArgumentParser(description= "This is our URL Spider")
parser.add_argument("input", help= "Specify a URL to search or a config file section")
parser.add_argument("-s" , help="Search Sting")
parser.add_argument("-c", help="Config File")
args= parser.parse_args()
# print(args)
# print(args.input)
# print(args.s)
# print(args.c)



if args.c is not None:
        config = configparser.ConfigParser()
        config.read(args.c)
        url = config[args.input]["url"]
        # print(url)

else:
        url = args.input
        # print(url)
        
if args.s is None:
        search_string = input("What do you want to search for? (If you want to match any URL, hit Enter): ")
else:
        search_string = args.s


url_regex = re.compile('"https?://.*?"')


site_request = requests.get(url)
site_data = site_request.text
for match in url_regex.findall(site_data):
    if search_string in match:
        print(match.strip('"'))

