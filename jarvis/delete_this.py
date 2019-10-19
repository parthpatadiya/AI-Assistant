# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 19:20:21 2019

@author: Microsoft
"""
import pyperclip
import os,keyboard,time
keyboard.press('win+e')
pyperclip.copy("parth soni")
#os.system('powershell.exe start C:')
os.startfile(".")
time.sleep(3)
keyboard.press('ctrl+f')
#k1=keyboard.add_hotkey('ctrl',print,args=['open explorer'])
#keyboard.press(k1)