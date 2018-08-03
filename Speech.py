from gtts import gTTS

import time
import pygame
import requests
import speech_recognition as sr

_WakeUpCommand = "Hey Grace"

def init():
    pygame.init()

def apiCallCheck(status):
    if status == requests.codes.ok:
        return 200
    else:
        return 404

## Calls the Grace api and filters the response 
# def getGraceQueryInfo()


## The output from Grace API 
# def printQueryResult
#     return queryResult

## Transcript of all recognised speech from Microphone input
def printTranscript(recognisedSpeech):
    print(recognisedSpeech)

def speak(response):
    textToSpeech = gTTS(text = response)
    textToSpeech.save("Grace Responce.AIFF")
    pygame.mixer.music.load("Grace Responce.AIFF")
    pygame.mixer.music.play()
    while(pygame.mixer.music.get_busy() == 1):
        time.sleep(1)


def listen():
    speech = sr.Recognizer()
    mic = sr.Microphone()
    audio = ""
    with mic as source:
        speech.adjust_for_ambient_noise(source)
        audio = speech.listen(source, phrase_time_limit=5)
    try:
        queryContence = speech.recognize_google(audio)
        return queryContence
    except sr.UnknownValueError:
        print("Speech Not Recognised")
    except sr.RequestError as e:
        print("Error: {0}" .format(e))


def wakeCommandCheck(recognisedText):

    if _WakeUpCommand.upper() in recognisedText.upper():
        return True
    else:
        return False

def main():
    init()
    while (True):
        wakeUp = False
        while(wakeUp == False):
            recognisedText = listen()
            printTranscript(recognisedText)
            if recognisedText is not None:
                wakeUp = wakeCommandCheck(recognisedText)
        
        speak("Hi, how can i help you?")
        
        query = False
        while (query == False):
            recognisedText = listen()
            printTranscript(recognisedSpeech)
            query = getGraceQueryInfo(recognisedText)
            output = printQueryResult()
            speak(output)


if __name__ == "__main__":
    main()