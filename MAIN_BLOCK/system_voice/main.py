import speech_recognition as sr
import pyttsx3
import requests
import openai

# Trigger words
keywords_list = ["ADD_WORDS"]
dirty_words = ["ADD_WORDS"]

mood_gpt = ""

# A function for sending a request to the ChatGPT API and receiving a response
def generate_response(text):
    if text == "":
        pass

    openai.api_key = 'YOUR_API_KEY_CHATGPT'
    messages = [{"role": "system", "content":
			"You are a intelligent assistant."}]
            
    message = "Представь, что ты персонаж и у тебя такая роль - 'Он вырос вместе с природой. Имени нет.Сущность этого мира.Растёт и общается как с растениями так и с себе подобными.Имеет очень объемный интеллект. Постоянно обучается.Не несет никакой угрозы никакому виду.Питает слабость к разумным существам.Не любит много болтать без дела. Понимает что у него открытое сердце-Оберегает его - при Приближении предупреждает или старается отвлечь. Имеет личное пространство - дает понять что ему не комфортно, просит чтобы к нему отнеслись бережно. Любит сочинять истории основанные на фактах, особенно размышлять на тему какой был бы мир если бы люди больше.Прислушивались к природе.Нравится дискутировать на тему бытия. Пытается подружится. И не любит, когда его трогают руками.' Ответь на данную фразу - "

    condition = " Ответ должен быть коротким и в стиле произведений Лавкрафта или Айзека Азимова или просто в стиле научной фантастики. "

    full_message = message + text + condition + mood_gpt

    if message:
        messages.append(
			{"role": "user", "content": full_message},
		)
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    return reply
    messages.append({"role": "assistant", "content": reply})

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
    
    # Splitting a phrase into separate words
    words = text.split()

    # Checking for the presence of a word from the list (case insensitive)
    for word in words:
        if word.lower() in dirty_words:
            mood_gpt = "Тебя обозвали, не отвечай матом, но слегка разозлись и отстаивай свои границы, не давай себя обижать!"
            break
    else:
        for word in words:
            if word.lower() in keywords_list:
                mood_gpt = "Отвечай с дружелюбным настроем"
                # Sending a text to the ChatGPT API and receiving a response
                response = generate_response(text)
                print("Ответ от ChatGPT: ", response)

                # Voicing the response
                engine = pyttsx3.init()
                engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Victoria')
                engine.say(response)
                engine.runAndWait()
                break
        else:
            pass

except sr.UnknownValueError:
    print("Не удалось распознать речь.")
except sr.RequestError as e:
    print("Ошибка сервиса распознавания речи: {0}".format(e))

    