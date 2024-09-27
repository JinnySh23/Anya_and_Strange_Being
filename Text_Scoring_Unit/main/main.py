import pyttsx3

# Creating an object for speech synthesis
engine = pyttsx3.init()

# Creating a voice synthesizer object
voices = engine.getProperty('voices')
# Sorting through the voices in Windows OS
for voice in voices:
    print(voice, voice.id)
    # Setting the speech language (if required)
    if voice.id == "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Victoria":

        engine.setProperty('voice', voice.id)

        # Opening a text file and reading the contents
        file_path = 'текст.txt'
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Text-to-speech
        engine.say(text)
        engine.runAndWait()
        # Stop
        engine.stop()