import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import time as tm 
import operator
from  gsearch.googlesearch import search 
from PyDictionary import PyDictionary


engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)
volume = engine.getProperty('volume')
engine.setProperty('volume', 2.0)
voices = engine.getProperty('voices')

#print(voices)
engine.setProperty('voice', voices[1].id)
bucketlist = []
notes = []



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        print("Good Morning")
        speak("Good Morning")
        
    elif hour >= 12 and hour < 18 :
        print("Good Afternoon")
        speak("Good Afternoon")
        
    else:
        print("Good Night")
        speak("Good Night")
        
    print("jarvis at your service")
    speak("jarvis at your service ")
    

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try :
        print("Recongnizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said : {query}\n " )
    except Exception as e:
        #print(e)


        print("Say it again please.....")
        return "none"
    return query

def countdown(n):
    while n > 0 :
        print(n)
        n = n - 1
        tm.sleep(1)
        if n == 0 :
            speak("Time Up")
    return takecommand()

def key(List):
    print("%s is being added" %List)
    speak("%s is being added" %List)
    bucketlist.append("%s" %List)
    speak("Added sir!")
    return takecommand()

def operation(op):
    return{
        '+' : operator.add,
        '-' : operator.sub,
        'x' : operator.mul,
        '/' : operator.__truediv__,
        'divided' : operator.__truediv__,
        'mod' : operator.mod,
        'Mod' : operator.mod,
        '^' : operator.xor,
    }[op]
def expression(op1, oper, op2):
    op1,op2 = int(op1),int(op2)
    return operation(oper)(op1,op2)

def note(notees):
    noteeess = notes.append(notees)
    speak("ok sir!")
    return takecommand()
def wordmeaning (word):
    result = dictionary.meaning(word)
    print(result)
    speak(result)
    return takecommand()



    


if __name__ == "__main__":
    
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
             speak("Searching in Wikipedia Sir")
             query = query.replace("wikipedia", "")
             results = wikipedia.summary(query, sentences = 2)
             speak("ok")
             speak("According to Wikipedia")
             print(results)
             speak(results)
        elif 'open youtube' in query:
             speak("ok")
             wb.open_new_tab('youtube.com')
        elif 'open google' in query:
            speak("ok")
            wb.open_new_tab('google.com')      

        elif "what's the time" in query:
            
            strtime = datetime.datetime.now().strftime("%H %M ")
            speak(f"Sir! The time is {strtime}\n")
        elif 'open code' in query:
            speak("ok")

            codepath = "C:\\Users\\Fsociety\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe "
            os.startfile(codepath)   
        elif  'open chrome' in query:
            speak("ok")
            browserpath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(browserpath)
        elif  'open browser' in query:
            speak("ok")
            browserpath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(browserpath)
        elif 'jarvis' in query:
            speak("At Your service sir!")
        elif ' text  file' in query:
            speak("ok")
            textfile = "C:\\windows\\system32\\notepad.exe"
            os.startfile(textfile)
        elif 'drop the needle' in query:
            speak("ok")
            music = "C:\\Users\\Fsociety\\Music"
            songs = os.listdir(music)
            os.startfile(os.path.join(music,songs [0]))
        elif 'set the timer' in query:
            speak('for how much time sir!')
            content = takecommand()
            num = int(content)
            print(num)
            
            speak('ok')
            s = num * 60
            countdown(s)
        elif 'list' in query:
            speak("what to add? sir")
            List = str(takecommand())
            key(List)
        elif "what is added" in query :
            speak(bucketlist)
        elif "who are you" in query:
            speak("I'm Jarvis, your assistant. just ask me what to do")
        elif "calculate" in query:
            speak("ok sir!")
            calculation = query.replace("calculate","")
            print(expression(*(calculation.split())))
            speak(expression(*(calculation.split())))
        
        elif 'note' in query : 
           notees = query.replace("note","")
           note(notees)
        elif 'log' in query :
            speak(notes)
        elif "meaning" in query:
            speak("ok sir")
            word  = query.replace("meaning","")            
            wordmeaning(word)

            
        elif 'shutdown' in query:
            break
            

    




         
        
        
        

        
    

   





