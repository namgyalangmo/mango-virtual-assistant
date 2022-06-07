import sys
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'mango' in command:
                command = command.replace('mango','')
                print(command)
    except:
        pass
    return command

def run_mango():
    command = take_command()
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk ('Current time is ' + time)

    elif ('how are you') or ('are you okay') in command:
        talk('I am having a great day ever since you started talking to me')

    elif ('joke') or ('tell me something funny') or ('make me laugh') in command:
        talk(pyjokes.get_joke())

    elif ('who is') or ('what is') or ('why is') in command:
        question = command.replace('who is', '')
        question = command.replace('what is', '')
        question = command.replace('why is', '')
        info = wikipedia.summary(question, 1)
        print(info)
        talk(info)
    else:
        talk('I am sorry I did not catch that, can you please repeat what you said?')

def end_program():
    talk('Is there anything else i can help you with?')
    command = take_command()

    if 'yes' in command:
        run_mango()
    else:
        talk('Okay! have a great day')
        sys.exit()



talk('Hi there! I am mango, your virtual assistant, How can I help you today')
run_mango()
end_program()
