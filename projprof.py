"""
Created on Wed Feb 19 19:35:52 2020

@author: leemshari
"""

import csv
import json

#List for filtered rows to go into
selected = []

#Open search criteria        
with open ('search.json', 'r') as filters:
    criteria = json.load(filters)
    
#Open and read in CSV file
with open ("CapitalProjectsDL.csv", 'r') as proj:
    reader = csv.DictReader(proj)

#Loop through CSV file and specifically pull out the criteria that I want
    for row in reader:

#I was interested in Facility Imporvement area
        if row['area']== criteria['area']:
#Here we are looking specifically for projects in 2018            
            if row['fiscal_year'] == criteria['fiscal_year']:

#Add filtered rows to list             
                    selected.append(row)
#Print list nicley            
print(json.dumps(selected, indent=4, sort_keys=True))  
    
