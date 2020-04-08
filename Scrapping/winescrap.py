#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 21:08:08 2020

@author: leemshari
"""

import urllib

from bs4 import BeautifulSoup


def getSearchURL(term,number):
    
    url = "https://www.wine.com/list/wine/%s/7155-106806/%d/" % (str(term),int(number))
        
    return url

def getPageText(url):
    
    req = urllib.request.Request(url)
    
    with urllib.request.urlopen(req) as response:
        
        return response.read()
    
def main():
    
    term = "spain"
    
    number = input("Please choose a page number between page 1 and page 11: ")
    print('')
    
    url = getSearchURL(term,number)
    
    pageText = getPageText(url)
    
    soup = BeautifulSoup(pageText, 'html.parser')
    
    wineatags = soup.find_all('a', 'prodItemInfo_link')
    
    winearating = soup.find_all('div', 'averageRating')
    
    title_list = []
    
    quality_list = []
    
    rating_dict = {}
    
    rating_sum = 0
    
    for rating in winearating:
        
        quality = rating.find('span').string
        
        quality = float(quality)
        
        rating_sum = rating_sum + quality
        
        quality_list.append(quality)
               
    totalTitles = 0
    
    for wine in wineatags:
    
        title = wine.find('span').string
        
        totalTitles = totalTitles + 1
        
        title_list.append(title)
        
    rating_dict = {title_list[i]: quality_list[i] for i in range(len(title_list))} 
    
    maximum =  rating_dict.get(max(rating_dict, key = rating_dict.get))  
    
    rating_list = []
    
    for key, value in rating_dict.items():
        
        if value == maximum:
            
            rating_list.append(key)
            
    print("The highest rated wine(s) on this page is:",*rating_list, sep = "\n")
    print('')
    
    print("With a rating of",maximum)
    print('')
    
    print("Out of",totalTitles,"wines on this page.")
    print('')
    
    print("And the average rating of wines on this page was",rating_sum/float(totalTitles))
   
main()
