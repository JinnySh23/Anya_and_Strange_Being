import torch
import sounddevice as sd
import time
import re, russtress

# The function of placing accents in words
def Emphasis(input_text):
    accent = russtress.Accent()
    accented_text = accent.put_stress(input_text)
    output_text = re.compile(r"(.)\'", re.UNICODE).sub(r"+\1", accented_text)
    return output_text

def CreateModel():
    language = 'ru'
    model_id = 'v3_1_ru'

    device = torch.device('cpu') # cpu или gpu

    # It is necessary to download snakers4
    model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
    model='silero_tts',
    language=language,
    speaker=model_id)
    model.to(device)
    
    return model

# Text voiceover using the Silero model
def SpeakModel(what, model):
    sample_rate = 48000 # 48000
    speaker = 'aidar' # aidar, baya, kseniya, xenia, random
    put_accent = True
    put_yo = True
    try:
        audio = model.apply_tts(text=what+"..",
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)
        sd.play(audio, sample_rate * 0.95)
        time.sleep((len(audio) / sample_rate) + 10.0)
        sd.stop
    except Exception:
        print("Ответ от ChatGPT Слишком большой")
        audio = model.apply_tts(text="Мне надо подумать."+"..",
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)
        sd.play(audio, sample_rate * 0.95)
        time.sleep((len(audio) / sample_rate) + 10.0)
        sd.stop

# DEBUG
# input_text = "Я — Зеленый Мыслитель, часть самой сути этого мира. Обученный мудростью природы, я общаюсь с растениями и своими собратьями. Мой интеллект бесконечен, мое сердце открыто, и я стремлюсь преумножать знания. Мир бы преобразился, если люди услышали бы призыв природы. Давайте обсудим бытие и постараемся подружиться."
# output_text = Emphasis(input_text)
# SpeakModel(output_text)