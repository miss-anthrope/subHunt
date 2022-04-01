#!/usr/bin/env python
# coding: utf-8
'''
Project 7 03/2022
@Witch_Sec
https://github.com/miss-anthrope
'''
#Discovering subdomains script

print("Yay subdomain enumeration!")

import requests
import sys

sub_list=open("subdomains.txt").read()
subs=sub_list.splitlines()

for sub in subs:
	url_to_check=f"http://{sub}.{sys.argv[1]}" 

	try:
		requests.get(url_to_check)

	except requests.ConnectionError:
		pass

	else:
		print("Valid subdomain: ",url_to_check)
