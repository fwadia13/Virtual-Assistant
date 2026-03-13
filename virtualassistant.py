import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)  # ✅ safe fallback

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = None  # ✅ initialize so return always works
    try:
        with sr.Microphone() as source:
            print("Calibrating for background noise...")
            listener.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = listener.listen(source)
            command = listener.recognize_google(audio).lower()  # ✅ lowercase for reliable matching
            print(f"You said: {command}")
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
    except sr.RequestError as e:
        print(f"Google API error: {e}")
    except OSError:
        print("Microphone not found or not accessible")
    return command

def run_Foris():
    command = take_command()
    if not command:  # ✅ guard against None before doing 'in' checks
        return
    if 'play' in command:
        song = command.replace('play', '').strip()
        speak('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f'The current time is {time}')
        print(time)
    elif 'who is' in command:
        person = command.replace('who is', '').strip()
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)
    elif 'joke' in command:
        joke = pyjokes.get_joke(language='en')
        print(joke)
        speak(joke)
    else:
        speak("Sorry, I didn't understand that command")

while True:
    run_Foris()
