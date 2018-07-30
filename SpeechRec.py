from gtts import gTTS
import os
import pygame, time
from pprint import pprint
import requests
import json

def init():
    pygame.init()
    

def apiCallCheck(status):
    if status == requests.codes.ok:
        return 200
    else:
        return 404

def getWeatherInfo(location):

    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + location + '&APPID=ae8cfbae2ade2a2e7f00d22fe4aa150b')
    status = apiCallCheck(r.status_code)
    
    if status == 200:
        weatherJson = json.loads(r.text)
        weather = weatherJson['weather'][0]["description"]
        temperature = weatherJson['main']["temp"]
        temperature = temperature - 273.15
        temperature = round(temperature,1)
        data = {"Location" : location, "Weather" : weather, "Temperature" : temperature}
        return data
    
    else:
        return -1

def printWeatherInfo(weatherInfo):
    print(weatherInfo['Location'])
    print(weatherInfo['Weather'])
    print(weatherInfo['Temperature'])

def speak(weatherInfo):
    tts = gTTS(text = "The weather for " + weatherInfo['Location'] + " is currently " + 
    weatherInfo['Weather'] + " with a temperature of " + str(weatherInfo['Temperature']) + " degrees")
    tts.save("weather.mp3")
    pygame.mixer.music.load("weather.mp3")
    pygame.mixer.music.play()
    while(pygame.mixer.music.get_busy() == 1):
        time.sleep(1)

def main():
    init()
    weatherQuery = True
    while(weatherQuery == True):
        location = input ("Enter a city for weather information: ")
        weatherInfo = getWeatherInfo(location)    
       
        if weatherInfo is not -1: 
            printWeatherInfo(weatherInfo)
            speak(weatherInfo)
        else:
            print("Error ")

        weather = input("Another weather Query?")
        if weather == 'n':
            tts = gTTS(text = "Goodbye")
            tts.save("goodbye.mp3")
            pygame.mixer.music.load("goodbye.mp3")
            pygame.mixer.music.play()
            while(pygame.mixer.music.get_busy() == 1):
                time.sleep(1)
            weatherQuery = False

    print("End of Program")
if __name__ == "__main__":
    main()
