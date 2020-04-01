#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 19:35:59 2020

@author: leemshari
"""

"""

Scrapping DEMO 


"""
import urllib

from bs4 import BeautifulSoup

def getSearchURL (term):
    
    url = "https://www.goodreads.com/search?q=%s&search_type=books" % (str(term))
    
    return url

def getPageText(url):
    
    req = urllib.request.Request(url)
    
    with urllib.request.urlopen(req) as response:
        
        return response.read()
    
def main():
    
    term = "virus"
    
    url = getSearchURL(term)
    
    pageText = getPageText(url)
    
    soup = BeautifulSoup(pageText, 'html.parser')
    
    bookatags = soup.find_all('a', 'bookTitle')
    
    print(bookatags)
    
    totalTitles = 0
    
    subTitles = 0
    
    for book in bookatags:
        
        title = book.find('span').string
        
        print(title)
        
        totalTitles = totalTitles + 1
        
        if ":" in title:
            
            subTitles = subTitles + 1
            
    print("Total titles: ",str(totalTitles))
    
    subts = subTitles/totalTitles*100
    
    print(str(subts), "% of books have subtitles")
    
main()
        