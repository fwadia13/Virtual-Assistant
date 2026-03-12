import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("Calibrating for background noise...")
            listener.adjust_for_ambient_noise(source, duration=1)
            print("Say something!")
            audio = listener.listen(source)
            command = listener.recognize_google(audio)
            print(command)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Google API error: {e}")
    except OSError:
        print("Microphone not found or not accessible")
    return command

def run_Foris():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        speak('Playing '+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f'The current time is {time}')
        print(time)
    elif 'who is ' in command:
        person = command.replace('who is ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)
    elif 'joke' in command:
        joke = pyjokes.get_joke(language='en')
        print(joke)
        speak(joke)
    else:
        speak('Sorry, I didn\'t understand that command')
while True:
    run_Foris()
