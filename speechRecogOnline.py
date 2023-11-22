"""
##### This is just a prototype project but you can use it to build many big projects thank you! #####

##########
visit github profile: https://github.com/TheCodarOfficial
github username: TheCodarOfficial
Author: TheCodarOfficial (Aniruddh Varun)
Launch Date on github: 22-11-2023
License: MIT License
##########

A) Commands to install python dependencies for this poject use terminals
like windows cmd, windows powershell, mac terminal, linux terminal etc...:
    1) command: pip install googletrans==3.1.0a0
    2) command: pip install SpeechRecognition
    3) command: pip install PyAudio
    4) command: pip install gTTS
    5) command: pip install playsound==1.2.2

[Optional]
    1) pip install pyttsx3
    2) pip install python-vlc (only if playsound==1.2.2 not works or giving error!)

B) Microphone should be enabled on any system/device and given access to work this programm

C) For more inf0 do checkout README.md file!

"""

import googletrans
import playsound
import speech_recognition
import speech_recognition as sr
import gtts

# import pyttsx3 # ignore if not uderstanding*

recognizer = speech_recognition.Recognizer()

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source, duration=5)
    print("Speak now!")
    voice = recognizer.listen(source)

    # listen = recognizer.recognize_google(voice,language="hi") # ignore if not uderstanding*

    listen = recognizer.recognize_google(voice,language="en")
    print(listen)

# print(googletrans.LANGUAGES) # ignore if not uderstanding*
# data = input("What is your name: ") # ignore if not uderstanding*

translator = googletrans.Translator()
translate = translator.translate(listen,dest="hi")
print(translate.text)
converted_audio = gtts.gTTS(translate.text,lang="hi")

# engine = pyttsx3.init() # ignore if not uderstanding*
# engine.say(translate.text) # ignore if not uderstanding*
# engine.runAndWait() # ignore if not uderstanding*

converted_audio.save("audio_tmp.mp3")
playsound.playsound("audio_tmp.mp3")