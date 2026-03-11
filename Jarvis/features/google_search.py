import webbrowser
import re
import urllib.parse
import pyttsx3


def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate', 180)


def google_search(command):
    reg_ex = re.search('search google for (.*)', command)
    if reg_ex:
        search_for = reg_ex.group(1)
    else:
        search_for = command.split("for", 1)[1]
    speak("Okay sir!")
    speak(f"Searching for {search_for}")
    url = 'https://www.google.com/search?q=' + urllib.parse.quote(search_for)
    webbrowser.open(url)