# -*- coding: utf-8 -*-
from speak_listen import speak,listen_command
import windows_query as winQ
import web_query as webQ
import wolframalpha
import os
import sys

def process_text(command):
    query = command
    # Logic for executing tasks based on query
    if 'music song' in query and 'next' in query:
        winQ.Music.next_music()
        return True
    elif 'previous' in query and 'music song' in query:
        winQ.Music.previous_music()
        return True
    elif 'play' in query and 'music song' in query:
        winQ.Music.play()
        return True
    elif 'the time' in query:
        winQ.wishMe.Time()
        return True
    elif 'open code' in query:
        codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
        return True
    elif ('bye' in query and 'jarvis' in query):
        speak('okay')
        speak('Bye Sir, have a good day.')
        sys.exit()
    elif 'search' in command:
        print("in search ")
        search_web(query)
    elif "who are you" in query or "define yourself" in query: 
        sp = '''Hello, I am Person. Your personal Assistant. 
        I am here to make your life easier. You can command me to perform 
        various tasks such as calculating sums or opening applications etcetra'''
        speak(sp) 
    elif "who made you" in query or "created you" in query: 
        sp = "I have been created by Parth and Karan."
        speak(sp) 
    elif "calculate" in query.lower():             
        # write your wolframalpha app_id here 
        app_id ='8QAHQL-2VG7J6RRYW'
        client = wolframalpha.Client(app_id) 
        indx = query.lower().split().index('calculate') 
        query = query.split()[indx + 1:] 
        res = client.query(' '.join(query)) 
        answer = next(res.results).text 
        speak("The answer is " + answer) 
    elif 'open' in query and 'software' in query: 
        pass
#            os.open("c:\\")
#            open_application(query.lower()) 
    else: 
        speak("I can search the web for you, Do you want to continue?") 
        ans = listen_command()
        if 'yes' in str(ans) or 'yeah' in str(ans): 
            search_web(query) 
        else:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
            print("after sys.exit()")            



def search_web(query): 
    print("query is ",query)
    if 'youtube' in query.lower(): 
        webQ.youtube(query)
    elif 'wikipedia' in query.lower(): 
        webQ.wikipedia(query)
    else:
        if 'google' in query.lower():
            ggl_query=query.lower()
            ggl_query=ggl_query.replace("search in google","")
            ggl_query=ggl_query.replace("google the","",1)
            ggl_query=ggl_query.replace("google","",1)
            webQ.google_search(ggl_query)
        elif 'search' in query.lower(): 
            ggl_query=ggl_query.replace("search","",1)
            webQ.google_search(ggl_query)

