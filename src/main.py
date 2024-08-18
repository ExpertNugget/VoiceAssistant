# GOAL: Make an AI voice assistant with multi input/output relative to the input location.
# Future goals would include task specific requests acting as different "personalities" to change speed, voice, and style of reply according to the task, as well as visual inputs/outputs for varied tasks.
import speech_recognition as sr


r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))