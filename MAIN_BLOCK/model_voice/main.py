import speech_recognition as sr
import pyttsx3
import requests
import openai
import voice_model
import time

# Trigger words
keywords_list = ["ADD_WORDS"]
# Obscene words
dirty_words = ["ADD_WORDS"]

mood_gpt = ""

# A function for sending a request to the ChatGPT API and receiving a response
def generate_response(text):
    if text == "":
        pass

    # API ключ от AI
    openai.api_key = 'YOUR_API_KEY_CHATGPT'

    message = "Представь, что ты персонаж и у тебя такая роль - 'Он вырос вместе с природой. Имени нет.Сущность этого мира.Растёт и общается как с растениями так и с себе подобными.Имеет очень объемный интеллект. Постоянно обучается.Не несет никакой угрозы никакому виду.Питает слабость к разумным существам.Не любит много болтать без дела. Понимает что у него открытое сердце-Оберегает его - при Приближении предупреждает или старается отвлечь. Имеет личное пространство - дает понять что ему не комфортно, просит чтобы к нему отнеслись бережно. Любит сочинять истории основанные на фактах, особенно размышлять на тему какой был бы мир если бы люди больше.Прислушивались к природе.Нравится дискутировать на тему бытия. Пытается подружится. И не любит, когда его трогают руками."
    # Сборка сообщения - запроса
    messages = [{"role": "system", "content":
			message + "Отвечай коротко"}]

    condition = " Ответ должен быть строго на русском, ответ должен быть коротким, не более 1000 символов и в стиле произведений Лавкрафта или Айзека Азимова или просто в стиле научной фантастики. "

    full_message = text + mood_gpt + condition

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


if __name__ == "__main__":

    # Initializing the voice model
    model = voice_model.CreateModel()

    # loop
    while 1:

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

            # Checking for the presence of a word from the list of mats (case insensitive)
            for word in words:
                if word.lower() in dirty_words:
                    # Setting the mood of ChatGPT
                    mood_gpt = "Тебя обозвали, не отвечай матом, но слегка разозлись и отстаивай свои границы, не давай себя обижать!"
                    # Sending a text to the ChatGPT API and receiving a response
                    response = generate_response(text)
                    print("Ответ от ChatGPT: ", response)
                    # We give an answer to the placement of accents
                    output_text = voice_model.Emphasis(response)
                    # We give the text with the accents placed on the voiceover of the Silero model
                    voice_model.SpeakModel(output_text, model)
                    break

                # Checking for the presence of a word from the list of trigger words (case insensitive)
                elif word.lower() in keywords_list:
                    # Setting the mood of ChatGPT
                    mood_gpt = "Отвечай с дружелюбным настроем"
                    # Sending a text to the ChatGPT API and receiving a response
                    response = generate_response(text)
                    print("Ответ от ChatGPT: ", response)
                    # We give an answer to the placement of accents
                    output_text = voice_model.Emphasis(response)
                    # We give the text with the accents placed on the voiceover of the Silero model
                    voice_model.SpeakModel(output_text, model)
                    break
                else:
                    pass

        except sr.UnknownValueError:
            print("Не удалось распознать речь.")
        except sr.RequestError as e:
            print("Ошибка сервиса распознавания речи: {0}".format(e))





    