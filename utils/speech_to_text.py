# File: utils/speech_to_text.py

import speech_recognition as sr

def transcribe_from_microphone():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source, timeout=5)
            return recognizer.recognize_google(audio)
        except sr.WaitTimeoutError:
            return "Sorry, no speech detected."
        except sr.UnknownValueError:
            return "Sorry, could not understand the audio."
        except sr.RequestError:
            return "Sorry, could not request results from the speech recognition service."
