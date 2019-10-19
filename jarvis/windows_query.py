# -*- coding: utf-8 -*-
import pyperclip
import os
import sys
import datetime
from speak_listen import speak
import keyboard
import mouse
import time
import subprocess

class WishMe:
    @staticmethod
    def walcome():
        speak("Welcome back sir")
        hour = int(datetime.datetime.now().hour)
        if hour>=6 and hour<12:
            speak("Good Morning!")
    
        elif hour>=12 and hour<18:
            speak("Good Afternoon!")
    
        elif hour>=18 and hour<24:
            speak("Good Evening!")    

        else:
            speak("Good Night!")            

        speak("Jarvis at your Service. Please tell me how can I help You ")
            
    @staticmethod
    def time():
        Time = datetime.datetime.now().strftime("%I:%M:%S") 
        speak("the current Time is")
        speak(Time)
    
    @staticmethod    
    def date():
        year = int(datetime.datetime.now().year)
        month = int(datetime.datetime.now().month)
        date = int(datetime.datetime.now().day)
        speak("the current Date is")
        speak(date)
        speak(month)
        speak(year)

class Music:
    no=0
    music_dir = 'C:\\Users\\Microsoft\\Music'
    songs = os.listdir(music_dir)
    def play():               
        os.startfile(os.path.join(Music.music_dir, Music.songs[Music.no]))
    def next_music():
        if Music.no<(len(Music.songs)-1):
            Music.no+=1
        else:
            Music.no=0
        Music.play()
    def previous_music():
        if Music.no>0:
            Music.no=Music.no-1
        else:
            Music.no=(len(Music.songs)-1)
        Music.play()
        
class FileSystem:
    def open_explorer(query):
        if 'open' in query:
            if 'explorer' in query or 'explorar' in query:
                os.open("Explorer")           
            if 'find' in query:
                os.open("Explorer")
                keyboard.press_and_release('ctrl+f')
                pyperclip.copy("abc")

class PcSettings:
    def shutdown():
        os.system('shutdown /s /f')
    def restart():
        os.system('shutdown /r /f')
    def wifi_on():
        os.system('powershell.exe Get-NetAdapter -Name WI-FI | Enable-NetAdapter')
        
    def wifi_off():
        p = subprocess.Popen(["powershell.exe","Get-NetAdapter -Name WI-FI | Disable-NetAdapter -Confirm:$false"], stdout=sys.stdout)
        p.communicate()
#        os.system("powershell -NoProfile -NoExit -Command notepad")
#        print(os.access("powershell.exe"))
#        pyperclip.copy("Get-NetAdapter -Name WI-FI | Disable-NetAdapter -Confirm:$false")
#        os.system("powershell.exe")
#        keyboard.press_and_release("alt+tab")
#        mouse.right_click()
#        keyboard.press_and_release("ctrl+v")
#        keyboard.press("\n")
        

PcSettings.wifi_off()