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
print(args)
print(args.input)
print(args.s)
print(args.c)

if args.c is not None:
        config = configparser.ConfigParser()
        config.read(args.c)
        url = config[args.input]["url"]
        print(url)

else:
        url = args.input
        print(url)
        

sys.exit()

#config = URL 
#searchstring
#config_file = Col_Gile.conf




url_regex = re.compile('"https?://.*?"')

#input_url = input("what url do you want to query: ")



search_string = input("what do you want to search for: ")


site_request = requests.get(input_url)
site_data = site_request.text
for match in url_regex.findall(site_data):
    if search_string in match:
        print(match.strip('"'))
