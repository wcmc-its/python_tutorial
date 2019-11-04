#!/usr/bin/python

import requests
import re
import configparser
import sys

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
