import requests
from yandex_speech import TTS

def speak(text, lang='ru', speaker='jane', emotion='neutral'):
    tts = TTS(text, lang, speaker, emotion)
    response = requests.get(tts.generate_url())
    if response.status_code == 200:
        with open('output.wav', 'wb') as f:
            f.write(response.content)

text = input('Введите текст для озвучивания: ')
speak(text)