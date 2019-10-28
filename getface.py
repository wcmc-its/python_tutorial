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

#input_url = input("what url do you want to query: ")

site_request = requests.get(input_url)

site_data = site_request.text

search_string = input("what do you want to search for: ")

url_regex = re.compile('"https?://.*?"')

for match in url_regex.findall(site_data):
    if search_string in match:
        print(match.strip('"'))
