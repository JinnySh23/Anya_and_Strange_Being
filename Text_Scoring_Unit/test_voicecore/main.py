import pyttsx3

# Creating an object for speech synthesis
engine = pyttsx3.init()

# Getting a list of available voice engines
voices = engine.getProperty('voices')

# We display information about each voice engine
for voice in voices:
    print("Имя: ", voice.name)
    print("ID: ", voice.id)
    print("Язык: ", voice.languages)
    print("Пол: ", voice.gender)
    print("Возраст: ", voice.age)
    print("\n")