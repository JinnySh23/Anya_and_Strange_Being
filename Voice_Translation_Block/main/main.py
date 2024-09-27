import speech_recognition as sr

# Creating a microphone object
r = sr.Recognizer()

# We receive audio from the microphone
with sr.Microphone() as source:
    print("Говорите сейчас...")
    audio = r.listen(source)
    print("Запись завершена.")

try:
    # Speech recognition
    text = r.recognize_google(audio, language='ru-RU')
    print("Распознанный текст: ", text)

    # Saving the translation in a text file
    with open("перевод.txt", "w") as file:
        file.write(text)
        print("Перевод сохранен в файл 'перевод.txt'.")

# Error handling
except sr.UnknownValueError:
    print("Не удалось распознать речь.")
except sr.RequestError as e:
    print("Ошибка сервиса распознавания речи; {0}".format(e))