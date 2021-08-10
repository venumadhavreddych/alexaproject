#speech recognition
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
from datetime import datetime
import pyjokes

#obtain audio from microphone

def talk(answer):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(answer)
    engine.runAndWait()
def processQuestion(question):
    if 'what are you doing' in question:
        print('I am waiting for your question..')
        talk('I am waiting for your question..')
        return True
    elif 'who are you' in question:
        print('I am Alexa and I am virtual talking friend')
        talk('I am Alexa and I am virtual talking friend')
        return True
    elif 'play' in question:
        question = question.replace('play', '')
        pywhatkit.playonyt(question)
        return True
    elif 'who is' in question:
        question = question.replace('who is', '')
        print(wikipedia.summary(question, 1))
        talk(wikipedia.summary(question, 1))
        return True
    elif 'time' in question:
        time = datetime.today().time().strftime('%I:%M %p')
        print(time)
        talk(time)
        return True
    elif "joke" in question:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
        return True
    elif 'love you' in question:
        talk('chepputho kodatha')
        return True
    elif "bye" in question:
        talk("Bye bye ,please take care.will meet you again later")
        return False
    else:
        print("I didn't get your question,can you say again.")
        return True
def getQuestion():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something")
        audio= r.listen(source)
    try:
        print(r.recognize_google(audio))
        question = r.recognize_google(audio)
        if 'Alexa' in question:
            question = question.replace('Alexa','')
            print(question)
            return question
        else:
            print('you are not talking with me, please carry on')
            return "notwithme"
    except sr.UnknownValueError:
         print("sorry, I cant get your question")
canAskQuestion = True
while canAskQuestion:
    question = getQuestion()
    if(question=="notwithme"):
        talk('Ok carry on with your friends,bye!')
        canAskQuestion=False
    else:
         canAskQuestion = processQuestion(question)