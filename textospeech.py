#text to speech in python
#RUN PIP INSTALL PY INSTALL PYTTSX3 FIRST
#import pyttsx (done in this lib)
import pyttsx3

#initalise
engine = pyttsx3.init()

#testing
engine.say("Replace this text with desired text to speech")
engine.say("The quick brown fox jumped over the lazy brown dog")
engine.say("These sentances can be expanded as desired")
engine.runAndWait()