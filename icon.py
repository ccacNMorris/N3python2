#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 18:34:05 2020

@author: leemshari
"""
# I wanted to create an n cubed icon
#My goal was to get this to get this to print with & or @ signs but I was unable to 
#get this array to look decent with anything but integers.
#I changed the dtype to str and the int_array[a,b] to @ but the array would be off 
import numpy as np
#function to pass in an array and tuple so that we can get image
def icon (tuple_list,int_array):
#tuple is basically coordinates for the image to populate in
    for a,b in tuple_list:
#I set the value that will populated at the coordinates to 3
        int_array[a,b] = 3

    return int_array

#function to manipulate arrary and elements in it
def roll_rotate(a_tuple,a_array):
#We want the array with the image to rotate and roll   
    b_array = icon(a_tuple,a_array)
#Numpy has different functions already built into it to manipulate arrays
    print(np.roll(b_array,1))
    
    print('')
    
    print(np.flipud(b_array))  
    
#Inention was to scale array up to 15x15 array    
def resize(b_tuple,b_array):
#Need to grab image again so that it can be manipulated   
    c_array = icon(b_tuple,b_array)
#Output makes the icon unreadable unfortunately but this numpy function will make it bigger    
    print(np.resize(c_array,(15,15)))

def main():
#Tuple that will be passed into the functions above
    image = ((0,6),(0,7),(0,8),(1,8),(2,7),(2,8),(3,8),(4,1),(4,6),(4,7),(4,8),
         (5,1),(5,2),(5,3),(5,4),(5,5),(6,1),(6,5),(7,1),(7,5),(8,1),(8,5),(9,1),(9,5))
#Array full of zeros that will be populated with 3s at correct coordinates
    image_array = np.zeros((10,10), dtype = int)
#printing image with tuple and array passed in
    print(icon(image,image_array))
 
    print('')
#Calling function to manipulate array   
    roll_rotate(image,image_array)
    
    print('')
#Calling function to scale array up    
    resize(image,image_array)

main()


