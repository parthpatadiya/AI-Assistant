# -*- coding: utf-8 -*-
from selenium import webdriver
#import selenium.webdriver.common.by as By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import smtplib
from speak_listen import speak

#import wikipedia
#import webbrowser
#import time

driver = webdriver.Chrome(executable_path="C:/Users/Microsoft/Desktop/chromedriver.exe")
    

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def map_search(place):
    prefix="https://www.google.co.in/maps/search/"
    driver.get(str(prefix+place))

def youtube(search): 
    speak("Opening in youtube")
    u_query=search.lower()
    u_query=u_query.replace("search in youtube","",1)
    u_query=u_query.replace("search youtube","",1)
    driver.get("http://www.youtube.com")
#    print("http://www.youtube.com/results?search_query =" + str(u_query))
    msgbox=WebDriverWait(driver,15).until(EC.visibility_of(driver.find_element_by_xpath('//*[@id="search"]')))
    msgbox.click()
    msgbox.send_keys(str(u_query))
    keyboard.press_and_release("\n")
#         another way to search directly search full query by url
#        driver.get("http://www.youtube.com/results?search_query="+str(u_query))
        
def wikipedia(search):
    wk_query=search.lower()
    wk_query=wk_query.replace("search in wikipedia","")
    wk_query=wk_query.replace("search wikipedia","",1)
    wk_query=wk_query.replace("wikipedia","",1)        
    driver.get("https://en.wikipedia.org/wiki/"+(search)) 
#        results = wikipedia.summary("mangal", sentences=2)
#        speak('Got it.')
#        speak('WIKIPEDIA says - ')
##        speak(results)

def google_search(search):
    driver.get("https://www.google.com/search?q ="+search)

    
    