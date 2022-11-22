import speech_recognition as sr
import pyttsx3


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
#             if 'sally' in command:
#                 command = command.replace('sally', 'sally')
#                 print(command)
    except:
        pass
    return command

def run_sally():
    command = take_command()

    print(command)

    if 'omega' in command:
        talk('Hello, please give me a command')
        
    elif 'who' and 'are' and 'you' in command:
        talk('I am Omega')
        
    else:
        talk('Please say something')

while True:
    run_sally()
