from gtts import gTTS
import json
import time
import pygame
import requests
import speech_recognition as sr



def init():
    pygame.init()

###Insert additional info from personal file###

## Request Auth token and SessionID for Grace
def getGraceSessionID():
    auth = requests.post(_AccountsURL, json = {"api_key":#"APIKEY HERE"})
    authJson = json.loads(auth.text)
    authToken = authJson['auth']["token"]

    auth = requests.post(_GraceURL + "/authenticate", json={"auth_token":authToken})
    
    sessionJson = json.loads(auth.text)
    sessionID = sessionJson["session_token"]
    return sessionID

## Send Query to Grace
def getGraceQueryInfo(sessionID, recognisedText):
    graceQuery = requests.post(_GraceURL + "/user_message",
        json={"message_body" : recognisedText, "message_key" : recognisedText},
        headers = {"Authorization" : sessionID}
        )
    return graceQuery.text

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

def graceStatus(statusResponse):
    print(statusResponse)
    if ("watson_midtree" in statusResponse):
        return False
    elif ("watson_completed" in statusResponse):
        return True

def graceLoop(sessionID):
    firstQuestion = True
    lastQuestion = False
    while (lastQuestion == False):
        if (firstQuestion):
            recognisedText = input("Enter a question: ")
            firstQuestion = False
        else:
            recognisedText = input("Response")
        
        statusResponse = getGraceQueryInfo(sessionID, recognisedText)
        lastQuestion = graceStatus(statusResponse)

def main():
    sessionID = getGraceSessionID()
    graceLoop(sessionID)
    # while(True):

    #     recognisedText = input("Enter a question: ")

        #text = getGraceQueryInfo(sessionID, recognisedText)
        #print(text)
        # if ("watson_midtree" in text):
        #     recognisedText = input("Responce: ")
        #     time.sleep(1)
        #     text = getGraceQueryInfo(sessionID, recognisedText)
    # init()
    # while (True):
    #     wakeUp = False
    #     while(wakeUp == False):
    #         recognisedText = listen()
    #         printTranscript(recognisedText)
    #         if recognisedText is not None:
    #             wakeUp = wakeCommandCheck(recognisedText)
        
    #     speak("Hi, how can i help you?")
    #     query = False
    #     while (query == False):
    #         recognisedText = listen()
    #         printTranscript(sessionID, recognisedSpeech)
    #         query = getGraceQueryInfo(recognisedText)
    #         output = printQueryResult()
    #         speak(output)


if __name__ == "__main__":
    main()
