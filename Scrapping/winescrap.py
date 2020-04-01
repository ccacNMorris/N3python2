#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 21:08:08 2020

@author: leemshari
"""

import urllib

from bs4 import BeautifulSoup

def getSearchURL (term):
    
    url = "https://www.wine.com/search?q=%s&search_type=region" % (str(term))
    
    return url

def getPageText(url):
    
    req = urllib.request.Request(url)
    
    with urllib.request.urlopen(req) as response:
        
        return response.read()
    
def main():
    
    term = "spain"
    
    url = getSearchURL(term)
    
    print(url)
    
    pageText = getPageText(url)
    
    soup = BeautifulSoup(pageText, 'html.parser')
    
    #print(soup)
    
    wineatags = soup.find_all('a', 'prodItemInfo_link')
    
    totalTitles = 0
    
    for wine in wineatags:
        
        title = wine.find('span').string
        
        print(title)
        
        print("")
        
        totalTitles = totalTitles + 1
        
    print("Number of titles on page 1:",totalTitles)
    
main()
        