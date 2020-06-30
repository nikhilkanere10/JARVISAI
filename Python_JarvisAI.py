import sys
import os
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import requests
import wikipedia
from gtts import gTTS

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id )
engine.setProperty('voice', voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning")
		
	elif hour>=12 and hour<18:
		speak("Good Afternoon")
		
	else:
		speak("Good Evening")
		
	speak("I am Jarvis")
	speak("please tell me how may i help you")
	
def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		r.energy_threshold = 700
		audio = r.listen(source)
		
	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language = 'en-in')
		print("User said: ", query)
		
	except Exception as e:
		print(e)
		print("Say that again please...")
		return "None"
		
	return query

if __name__ == '__main__':
	wishMe()
	
	while True:
		query = takeCommand().lower()
		
		if 'Wikipedia' in query:
			speak("Searching wikipedia...")
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences=2)
			speak("According to wikipedia")
			print(results)
			speak(results)
			
		elif 'open youtube' in query:
			webbrowser.open("youtube.com")
			speak('this is the about page')
				
		elif 'open google' in query:
			webbrowser.open("google.com")
			speak('this is the about page')
			
		elif 'open towardsdatascience' in query:
			webbrowser.open("towardsdatascience.com")
			speak('this is the about page')
			
		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			speak(f'Sir, the time is {strTime}')	
				
		else:
			speak("can you please repeat that")
			
if __name__ == "__main__":
    wishMe()
    takeCommand()
			
			
    
	
	
