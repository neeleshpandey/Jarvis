import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyjokes
import os
from newsapi import NewsApiClient
from random import randint

BOSS = "Neelesh"
NEWS_API_KEY = "" #Add NEWS API Here

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(txt):
    engine.setProperty("rate", 150)  
    engine.say(txt)
    engine.runAndWait()

def time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def wishMe():
    hour = int(time().split(":")[0])
    if hour >=0 and hour < 12:
        speak("Good Morning ")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon ")
    else:
        speak("Good Evening ")
    speak(f"boss ,the time is {time()}")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language = 'en-in')
        print("user said: ",query, end='\n')

    except Exception as e:
        print(e)
        print("say that again please.....")
        return "None"
    return query




if __name__ =="__main__":
    speak("I am online")
    wishMe()
    while True:
        query = takecommand().lower()
        if 'jarvis' in query:
            if "wikipedia" in query or "who is" in query:
                try:
                    speak("searching wikipedia")
                    query = query.replace("who is","")
                    query = query.replace("search","")
                    query = query.replace("on","")
                    query = query.replace("wikipedia","")
                    query = query.replace("jarvis","")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    print(results)
                    speak(results)
                except:
                    speak("There is some trouble in searching, sorry for inconvenience")

            elif "open youtube" in query:
                speak("Here you go to Youtube")
                webbrowser.open("https://youtube.com")

            elif "open amazon" in query:
                speak("Here you go to amazon")
                webbrowser.open("https://amazon.com")

            elif "open flipkart" in query:
                speak("Here you go to flipkart")
                webbrowser.open("https://flipkart.com")

            elif "open gmail" in query:
                speak("Here you go to gmail")
                webbrowser.open("https://mail.google.com/")
            
            elif "open google" in query:
                speak("Here you go to google")
                webbrowser.open("google.com")

            elif 'play music' in query or "play song" in query:
                speak("Here you go with music")
                music_dir = ""  #Directory where music is stored
                songs = os.listdir(music_dir)
                i = 1
                for song in songs:
                    print(str(i)+". "+song)   
                os.startfile(os.path.join(music_dir, songs[randint(0,i-1)]))

            elif "the time" in query:
                speak(f"boss ,the time is {time()}")

            elif "joke" in query:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

            elif "who i am" in query:
                speak("If you talk then definitely your human.")
    
            elif "what are you" in query or "who are you" in query:
                speak("I am Virtual being, My name is Jarvis")
                speak(f"My creator is {BOSS}. further my identity, It's a secret")
                speak("May be i am a baby ultron")
                speak("HaHaHahahh")
            
            elif 'is love' in query:
                speak("It is 7th sense that destroy all other senses")
            
            elif 'how are you' in query:
                speak("I am fine, Thank you")
                speak("How are you, Sir")
    
            elif 'fine' in query or "good" in query:
                speak("It's good to know that your fine")
            
            elif "jarvis" == query:
                wishMe()
                speak(f"Jarvis 1 point o in your service Mister {BOSS}")
            
            elif "news" in query or "headlines" in query:
                try:
                    newsapi = NewsApiClient(api_key= NEWS_API_KEY)
                    all_articles = newsapi.get_top_headlines(language='en')
                except Exception as e:
                    speak("There is some problem with NEWS API")
                    print("The ERROR is",e,sep="\n")
                    continue
                i = 1
                speak("The Top Headlines are")
                for article in all_articles['articles']:
                    speak(str(i)+" "+article['title']+" "+article['description'])
                    if(i == 5):
                        break
                    i += 1
                
            elif "i love you" in query:
                speak("Hmmmmmmmm... I understand, but I am engaged with siri, I'll let you know in case of breakup, till then i can play some videos for you")
            
            elif "sleep" in query:
                speak("Yes Boss, I am taking a nap")
                break
            
        else:
            continue
