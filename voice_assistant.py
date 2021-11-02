import subprocess
import pyttsx3
import json
import instaloader
import random
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywikihow
import winshell
import pyjokes
import feedparser
import wolframalpha
import ctypes
import time
import requests
from requests import get
import shutil
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import cv2
import random
import pyautogui
import PyPDF2
import playsound
import socket
# import pywhatkit
import operator

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !")

	else:
		speak("Good Evening Sir !")

	assname = ("Jarvis 1 point o")
	speak("I am your Assistant")
	speak(assname)

def usrname():
	speak("What should i call you sir")
	uname = takeCommand()
	speak("Welcome Mister")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	
	print("#####################".center(columns))
	print("Welcome Mr.", uname.center(columns))
	print("#####################".center(columns))
	
	speak("How can i Help you, Sir")

# def pdf_reader():
#     book = open('py3.pdf', 'rb')
#     pdfReader = PyPDF2.PdfFileReader(book)
#     pages = pdfReader.numPages
#     speak(f"Total numbers of pages in this book {pages}")
#     speak('sir please enter the page number i have to read')
#     pg = int(input("Please enter the page number: "))
#     page = pdfReader.getPage(pg)
#     text = page.extractText()
#     speak(text)



def takeCommand():
	
	r = sr.Recognizer()

	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"
	
	return query

if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    usrname()
     
    while True:
         
        query = takeCommand().lower()
         
        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
 
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'search in google' in query:
            speak("What you want search in Google")
            command = takeCommand()
            url = 'https://google.com/search?q=' + command
            webbrowser.get().open(url)
            # webbrowser.open('https://google.com/search?q=' + command)
            

        # elif 'search in google' in query:
        #     speak("What you want search in Google")
        #     command = takeCommand()
        #     webbrowser.open(f"{command}")

        elif "search in wiki" in query:
            speak("What you want search in Wikipedia")
            command = takeCommand()
            # url = 'https://wikipedia.org/search?q=' + command
            url = 'https://en.wikipedia.org/wiki/' + command
            webbrowser.get().open(url)
            # webbrowser.open("wikipedia.com")

        elif 'laughing' in query:
            speak('HAHAHAHA')
 
        elif 'open stack overflow' in query:
            speak("Here you go to Stack Over flow  Happy coding")
            webbrowser.open("stackoverflow.com")  
 
        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            music_dir = "E:\\playlist"
            songs = os.listdir(music_dir) 
            random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir, random_song))
 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")   
            speak(f"Sir, the time is {strTime}")
 
 
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
 
        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")
 
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)
 
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
 
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Lucky.")
             
        elif 'joke' in query:
            jokes = pyjokes.get_joke()
            print(jokes)
            speak(jokes)
 
        elif "who i am" in query:
            speak("If you talk then definately you are human.")
 
        elif "why you came to world" in query:
            speak("Thanks to Lucky. further It's a secret")
 
        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
 
        elif "who are you" in query:
            speak("I am your virtual assistant created by Lucky")
 
        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister Lucky")
 
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "E:\\wallpaper\\groot.jpg",
                                                       0)
            speak("Background changed succesfully")
 
         
        # elif 'lock window' in query:
        #         speak("locking the device")
        #         ctypes.windll.user32.LockWorkStation()
 
        # elif 'shutdown system' in query:
        #         speak("Hold On a Sec ! Your system is on its way to shut down")
        #         subprocess.call('shutdown / p /f')
                 
        # elif 'empty recycle bin' in query:
        #     winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
        #     speak("Recycle Bin Recycled")
        #     winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            
 
        # elif "don't listen" in query or "stop listening" in query:
        #     speak("for how much time you want to stop jarvis from listening commands")
        #     a = int(takeCommand())
        #     time.sleep(a)
        #     print(a)
 
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://google.nl/maps/place/" + location + "")
 
        # elif "restart" in query:
        #     subprocess.call(["shutdown", "/r"])
             
        elif "jarvis" in query:
             
            wishMe()
            speak("Jarvis 1 point o in your service Mister")
            # speak(assname)

        elif 'weather' in query:
            user_api = 'af49bdaf9a5238b276ea1289c5882b7a'
            speak('Tell me city name: ')
            location = takeCommand()
            complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
            api_link = requests.get(complete_api_link)
            api_data = api_link.json()
            
            #create variables to store and display data
            temp_city = ((api_data['main']['temp']) - 273.15)
            weather_desc = api_data['weather'][0]['description']
            hmdt = api_data['main']['humidity']
            wind_spd = api_data['wind']['speed']
            date_time = datetime.datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

            print ("-------------------------------------------------------------")
            print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
            print ("-------------------------------------------------------------")

            print ("Current temperature is: {:.2f} deg C".format(temp_city))
            print ("Current weather desc  :",weather_desc)
            print ("Current Humidity      :",hmdt, '%')
            print ("Current wind speed    :",wind_spd ,'kmph')

        elif "i love you" in query:
            speak("It's hard to understand")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "ip address" in query:
            # ip = get('https://api.ipify.org').text
            # print(ip)
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            print(ip)
            speak(f"Your IP Address is {ip}")
        
        elif "change window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif 'volume up' in query:
            pyautogui.press('volumeup')

        elif 'volume down' in query:
            pyautogui.press('volumedown')
        
        elif 'volume mute' in query:
            pyautogui.press('volumemute')

        # elif "send message" in query:
        #     speak('sending')
        #     pywhatkit.sendwhatmsg("+919687870326", "hi", 11, 49)

        # elif "tell me news" in query:
        #     speak("Please wait sir, fetching the latest news")
        #     news()

        elif "news" in query:
            r = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=b5ab09b8750549a38f521647efbf7b93')
            # print(r.content)
            data = json.loads(r.content)
            for i in range(3):
                News = data['articles'][i]['title']
                print("News", i + 1, ":", News)
                speak(News)

        elif 'where i am' in query or 'where we are' in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                # hostname = socket.gethostname()
                # ip = socket.gethostbyname(hostname)
                # print(ip)
                url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                print(f"Sir I am not sure, but i think we are in {city} city of {country} country")
                speak(f"Sir I am not sure, but i think we are in {city} city of {country} country")
                
            except Exception as e:
                speak("Sorry sir, Due to network issue i am not able to find where we are.")
                pass

        
        
        # elif 'read pdf' in query:
        #     pdf_reader()
    
        elif 'instagram profile' in query or 'profile on instagram' in query:
            speak('sir please enter the user name correctly.')
            name = input('Enter usename here:')
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Sir here is the profile of the user {name}")
            
        elif 'send message' in query:
            speak('sir what should i say')
            msz = takeCommand()
            from twilio.rest import Client
            account_sid = 'AC77893dd604abca839f9c5ea9be164aa8'
            auth_token =  '6d6cc8392bc6c1418d25d62a53972e89'
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                    body = msz,
                    from_ = '+14432947120',
                    to = '+916354572088'
                    )
            print(message.sid)
            speak('sir, message has been sent')

        # elif 'do some calculation' in query or 'can you calculate' in query:
        #     r = sr.Recognizer()
        #     with sr.Microphone() as source:
        #         speak("Say what you want to calculate, example: 3 plus 3")
        #         print("listening...")
        #         r.adjust_for_ambient_noise(source)
        #         audio = r.listen(source)
        #     my_string = r.recognize_google(audio)
        #     print(my_string)

        #     def get_operator_fn(op):
        #         return{
        #             '+' : operator.add, # plus
        #             '-' : operator.sub, # minus
        #             'x' : operator.mul, # multiplied by
        #             'divided' : operator.__truediv__, # divided

        #         }[op]
            
        #     def eval_binary_expr(op1, oper, op2):
        #         op1, op2 = int(op1), int(op2)
        #         return get_operator_fn(oper)(op1, op2)
        #     speak('your result is')
        #     ans = eval_binary_expr(*(my_string.split()))
        #     print(ans)
        #     speak(eval_binary_expr(*(my_string.split())))


        elif 'activate how to mod' in query:
            from pywikihow import search_wikihow
            speak('How to do mod is activated')
            while True:
                speak('please tell me what you want to know')
                how = takeCommand()
                try:
                    if 'exit' in how or 'close' in how:
                        speak('okay sir, how to do mode is closed')
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)

                except Exception as e:
                    speak('sorry sir, I am not able to find this')

        # elif 'take screenshot' in query or 'take a screenshot':
        #     speak('sir, please tell me the name for this screenshot file')
        #     name = takeCommand()
        #     speak('please sir hold the screen for seconds, i am taking screenshot')
        #     time.sleep(3)
        #     img = pyautogui.screenshot()
        #     img.save(f'{name}.png')
        #     speak('I am done sir, the screenshot is saved in out main folder. I am ready for next command')
        
        elif "ask question" in query:
            # Taking input from user
            # question = input('Question: ')
            speak('Ask Your Question')
            try:
                question = takeCommand()
                speak(question)
                
                # App id obtained by the above steps
                app_id = 'LVKATJ-R59W32J8TR'
  
                # Instance of wolf ram alpha 
                # client class
                client = wolframalpha.Client(app_id)
  
                # Stores the response from 
                # wolf ram alpha
                res = client.query(question)
  
                # Includes only text from the response
                answer = next(res.results).text
  
                print('Your Answer is: ', answer)
                speak(f'Your Answer is: {answer}')

            except Exception as e:
                speak('Sorry I am not able to find the answer of your question')
 