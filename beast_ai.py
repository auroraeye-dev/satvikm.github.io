import speech_recognition as sr
import webbrowser
import pyttsx3
import subprocess
import musiclibrary
import requests
from newsapi import NewsApiClient
from openai import OpenAI
import pyautogui
import time

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Replace with your actual News API key
api = NewsApiClient(api_key="YOUR_NEWS_API_KEY_HERE")

def aiprocess(command):
    # Replace with your actual OpenAI API key
    client = OpenAI(api_key="YOUR_OPENAI_API_KEY_HERE")

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message.content

def try_skip_ad(image_path="YOUR_IMAGE_PATH.png", timeout=15):
    """
    Placeholder version. Full skip logic hidden for privacy.
    """
    print("Ad skipping feature is private and not included in this public version.")

    if not match:
        print("No Skip Ad button found after 30 seconds. Carrying on...")

if __name__ == "__main__":
    speak("Beast Activated")
    while True:
        r = sr.Recognizer()
        recognizer.energy_threshold = 300

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            command = r.recognize_google(audio)
            print("You said:", command)

            if command.lower() == "wake up":
                speak("Beast is ready. Listening for your command now.")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=3)
                    command = r.recognize_google(audio)
                    print("You said:", command)

                    if "open youtube" in command.lower():
                        speak("opening youtube")
                        webbrowser.open("https://www.youtube.com")

                    elif "open google" in command.lower():
                        speak("opening google")
                        webbrowser.open("https://www.google.com")

                    elif "open facebook" in command.lower():
                        speak("opening facebook")
                        webbrowser.open("https://www.facebook.com")

                    elif "open twitter" in command.lower():
                        speak("opening twitter")
                        webbrowser.open("https://www.twitter.com")

                    elif "open instagram" in command.lower():
                        speak("opening instagram")
                        webbrowser.open("https://www.instagram.com")

                    elif "open sticky notes" in command.lower():
                        speak("opening sticky notes")
                        subprocess.Popen("explorer.exe shell:appsFolder\\STICKY_NOTES_APP_ID_HERE")

                    elif "play" in command.lower():
                        song = command.lower().split(" ")[1]
                        link = musiclibrary.music[song]
                        speak("playing {}".format(song))
                        webbrowser.open(link)
                        try_skip_ad("FULL_PATH_TO_SKIP_AD_IMAGE.png")

                    elif "news" in command.lower():
                        speak("Fetching latest news headlines")
                        data = api.get_top_headlines(language='en', page_size=1)
                        types = data['articles']
                        for type in types:
                            title = type['title']
                            description = type['description']
                            speak("Title: " + title + ". Description: " + description)

                    elif "search" in command.lower():
                        query = command.lower().split(" ")[1]
                        speak("Searching for {}".format(query))
                        webbrowser.open("https://www.google.com/search?q={}&rlz=1C1ONGR_enIN1017IN1017&oq={}&gs_lcrp=...".format(query, query))

                    elif "google" in command.lower():
                        words = command.split(" ")
                        query_words = words[1:]
                        query = "+".join(query_words)
                        url = f"https://www.google.com/search?q={query}"
                        webbrowser.open(url)

                    else:
                        output = aiprocess(command)
                        speak(output)

        except Exception as e:
            print("error {}".format(e))
