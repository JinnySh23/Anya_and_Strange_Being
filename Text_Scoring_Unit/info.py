# In the pyttsx3 library, you can set up various voiceover voices. 
# The library uses the voices available in the operating system, so the available voice options depend on the platform, 
# on which the program is running.

import pyttsx3

engine = pyttsx3.init()

# We get a list of available votes
voices = engine.getProperty('voices')

# We display information about each voice
for voice in voices:
    print("Имя: %s" % voice.name)
    print("ID: %s" % voice.id)
    print("Язык(и): %s" % voice.languages)
    print("Пол: %s" % voice.gender)
    print("Возраст: %s" % voice.age)
    print("\n")


# Setting the voice by its ID
engine.setProperty('voice', 'идентификатор_голоса')
engine.setProperty('voice', voices[0].id)