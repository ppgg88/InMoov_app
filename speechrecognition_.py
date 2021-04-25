import speech_recognition as sr

rec_vocal = sr.Recognizer()
mic = sr.Microphone()
rec_vocal.pause_threshold = 0.5
rec_vocal.non_speaking_duration = 0.4

init_mic = False

def speak_recognition():
    global init_mic
    with mic as src:
        if init_mic == False:
            rec_vocal.adjust_for_ambient_noise(src, duration=2)
            print("ok")
            init_mic = True
        audio = rec_vocal.listen(src)
        try :
            text = rec_vocal.recognize_google(audio, language="fr-FR")
            print(text)
        except:
            pass
