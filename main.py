import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "33b8ac333a414c79972f6786b2698152"

def speak(text):
  engine.say(text)
  engine.runAndWait()

def processCommand(c):
  if "open google" in c.lower():
    webbrowser.open("https://www.google.com/")  
  elif "open youtube" in c.lower():
    webbrowser.open("https://www.youtube.com/") 
  elif "open chatgpt" in c.lower():
    webbrowser.open("https://chatgpt.com/") 
  elif "open linkedin" in c.lower():
    webbrowser.open("https://www.linkedin.com/") 
  elif c.lower().startswith("play"):
    song = c.lower().split(" ")[1]
    link = musicLibrary.music[song]
    webbrowser.open(link)

  elif "news" in c.lower():
    r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=33b8ac333a414c79972f6786b2698152")
    if r.status_code == 200:
      data = r.json()

      articles= data.get('articles',[])

      for article in articles:
        speak(article['title'])

  # else:
    #Let openai handle the request
     
if __name__ == "__main__":
  speak("Initializing Strain...")
  while True:

    r = sr.Recognizer()

    print("recognizing....")
    try:
      with sr.Microphone()as source:
        print("Listening...")
        audio = r.listen(source, timeout=2, phrase_time_limit=1)
      word = r.recognize_google(audio)
      if(word.lower()=='strain'):
        speak("Ya")
        with sr.Microphone() as source:
          print("Strain Active...")
          audio = r.listen(source)
          command = r.recognize_google(audio)

          processCommand(command)

    except Exception as e:
      print("Error; {0}".format(e))      