#!/usr/bin/python

import requests
import re
import configparser
import sys
import argparse

parser = argparse.ArgumentParser(description= "This is our URL Spider")
parser.add_argument("input_url")
parser.add_argument("-s" , help="Search Sting")
parser.add_argument("-c", help="Config File")
args= parser.parse_args()
print(args)
print(args.input_url)
print(args.s)
print(args.c)

sys.exit()

#config = URL 
#searchstring
#config_file = Col_Gile.conf



arguments = sys.argv
section = arguments[1]

config = configparser.ConfigParser()
config.read("config.conf")
input_url = config[section]["url"]

url_regex = re.compile('"https?://.*?"')

#input_url = input("what url do you want to query: ")



search_string = input("what do you want to search for: ")


site_request = requests.get(input_url)
site_data = site_request.text
for match in url_regex.findall(site_data):
    if search_string in match:
        print(match.strip('"'))
