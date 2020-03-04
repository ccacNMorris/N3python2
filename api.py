#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 20:08:50 2020

@author: leemshari
"""
import pprint
import requests, json

cheapest = []
user_add = input('Put in any zip code:')

payload = {'zip': user_add}

req = requests.get('http://opentable.herokuapp.com/api/restaurants', params=payload)

if(int(req.status_code) == 200):
#     print(req.headers.keys())
    apiDict = json.loads(req.text)
    
    pprint.pprint(apiDict)

for key in apiDict:
    
    if apiDict["price"] == '1':
    
        cheapest.append(key)
    
    if apiDict["price"] == '2':
    
        cheapest.append(key)
    
print(json.dumps(cheapest, indent=4, sort_keys=True)) 
    
