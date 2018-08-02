import speech_recognition as sr

_AudioFile = ("weather.wav")
_WakeUpCommand = "wather"

# def getWakeUp(_WakeUpCommand):
#     return wakeUpCommand = _WakeUpCommand

# def getAudioFile(_AudioFile):
#     return audioFile = _AudioFile


# r = sr.Recognizer()
# with sr.AudioFile(AUDIO_FILE) as source:
#     audio = r.record(source)
# try:
#     print("The audio file contains: " + r.recognize_google(audio))
#     queryContence = r.recognize_google(audio)
#     if "weather" in queryContence:
#         print("")
        
# except sr.UnknownValueError:
#     print("Not recognised")
# except sr.RequestError as e:
#     print("Error: {0}" .format(e))

# def init():

# def apiCallCheck(status):

# def getWeatherInfo(location)

# def printWeatherInfo():

# def printTranscript():

# def speak():

def listen():
    recognise = sr.Recognizer()
    with sr.AudioFile(_AudioFile) as source:
        audio = recognise.record(source)
    try:
        queryContence = recognise.recognize_google(audio)
        return queryContence
    except sr.UnknownValueError:
        print("Not Recognised")
    except sr.RequestError as e:
        print("Error: {0}" .format(e))



#def wakeCommandCheck():

def main():
    wakeUp = False
    while(wakeUp == False):
        recognisedText = listen()
        if _WakeUpCommand in recognisedText:
             print("Recognised")
             wakeUp = True
        else:
            print("Not Recognised")
    print("New Statement")

if __name__ == "__main__":
    main()