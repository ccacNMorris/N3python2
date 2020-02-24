#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 22:40:26 2020

@author: leemshari
"""

import csv

#def process311Data():
    
file = open('pgh311Abbrev.csv',newline='')
    
reader = csv.DictReader(file)
    
countPublic = {'Call Center': 0, 'Website': 0, 'Control Panel': 0}

countDistrict = {}

for row in reader:
        
    if row['REQUEST_ORIGIN'] == 'Call Center':

        countPublic['Call Center'] = countPublic['Call Center'] + 1
        
    elif row['REQUEST_ORIGIN'] == 'Website':
        
          countPublic['Website'] = countPublic['Website'] + 1
    
    elif row['REQUEST_ORIGIN'] == 'Control Panel':
    
          countPublic['Control Panel'] = countPublic['Control Panel'] + 1
    
    for number in row['PUBLIC_WORKS_DIVISION']:
        
        if number in countDistrict:

            countDistrict[number] =  countDistrict[number] + 1     
        
        else:
            
            countDistrict[number] = 1
    
 
file.close()

print(countPublic)

print(f'{"District":<}','','Occurences')

for number, count in sorted(countDistrict.items()):
    print(f' {number:<12}{count}')
               



