#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 20:08:50 2020

@author: leemshari
"""
import pprint
import requests, json

cheapest = []
# user_add = input('Put in any zip code:')
zipcode = 15201
while zipcode <= 15295:

    payload = {'zip': zipcode}

    req = requests.get('http://opentable.herokuapp.com/api/restaurants', params=payload)

    if(int(req.status_code) == 200):
    #     print(req.headers.keys())
        apiDict = json.loads(req.text)

        # pprint.pprint(apiDict)

        for key in apiDict['restaurants']:

            if key["price"] == 3:

                cheapest.append(key)

            if key["price"] == 4:

                cheapest.append(key)
    zipcode += 1
    print('... Thinking')
print(json.dumps(cheapest, indent=4, sort_keys=True))


# with open('restaurants_cheapest.json', 'w') as out_file:
#     json.dump(cheapest, out_file, indent=3)

with open('restaurants_expensive.json', 'w') as out_file:
    json.dump(cheapest, out_file, indent=3)