import schedule
import time
import os
import pyttsx3
from datetime import datetime

# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()
start_time = datetime.now()
distime = start_time.strftime("%I:%M %p")

voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[11].id) #Englist male voice 

# List of female voices: Also you can play around by adding the +f1 to +f4 with other basic voices. For more info you can check this issue in github : pyttsx female voice.

# engine.setProperty('voice', 'english+f1')
engine.setProperty('voice', 'english+f2')
# engine.setProperty('voice', 'english+f3')
# engine.setProperty('voice', 'english+f4')
# engine.setProperty('voice', 'english_rp+f3') #my preference
# engine.setProperty('voice', 'english_rp+f4')

# To get the list of voices present uncomment this code and run
# index = 0
# for voice in voices:
#    print(f'index-> {index} -- {voice.name}')
#    index +=1

def speaktime():
    # say method on the engine that passing input text to be spoken
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    engine.say('Time now is '+current_time)

    if(current_time>='12:00AM'):
        engine.say("Fill your timesheet and go to sleep")
    
    if(current_time>'01:00PM'):
        engine.say("Fill AXTRIA recruitment form")
    # run and wait method, it processes the voice commands.
    if(distime<current_time):
        print(current_time)
    engine.runAndWait()

def displaytime():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")

    if(distime<current_time):
        print(current_time)

schedule.every(30).minutes.do(displaytime)
# schedule.every(1).second.do(timeon)
schedule.every(1).hour.do(speaktime)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
