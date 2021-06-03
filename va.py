import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sounddevice

try:
    listener = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[17].id)


    def talk(text):
        engine.say(text)
        engine.runAndWait()


    def take_command():
        try:
            with sr.Microphone() as source:
                print('Hey! Please Speak')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'pi' in command:
                    command = command.replace('pi', '')
                    print(command)
        except:
            pass
        return command


    def run_pi():
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print('Current Time is ' + time)
            talk('Current Time is' + time)
        elif 'date' in command:
            date = datetime.datetime.now().strftime('%d:%B:%y')
            print('Today is ' + date)
            talk('Today is' + date)
        elif ('search' in command) or ('find' in command):
            search = command.replace('search', '').replace('find', '')
            pywhatkit.search(search)
            talk(search)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            print(joke)
            talk(joke)
        else:
            talk('Please Say Again!')
            print('Please Say Again!')


    while True:
        run_pi()

except KeyboardInterrupt:
    pass
