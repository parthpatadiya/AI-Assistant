# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 12:40:41 2019

@author: Microsoft
"""

# Python program to get a google map 
# image of specified location using 
# Google Static Maps API 

# importing required modules 
import requests 

# Enter your api key here 
api_key = "QaRm5PWevwSXQss5IzbZntRkwac"

# url variable store url 
url = "https://maps.googleapis.com/maps/api/staticmap?"

# center defines the center of the map, 
# equidistant from all edges of the map. 
center = "Dehradun"

# zoom defines the zoom 
# level of the map 
zoom = 10

# get method of requests module 
# return response object 
r = requests.get(url + "center =" + center + "&zoom =" +
				str(zoom) + "&size = 400x400&key =" +
							api_key + "sensor = false") 
print(r.content)