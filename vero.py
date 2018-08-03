import win32com.client as wincl
import time
import random
import speech_recognition as sr

r = sr.Recognizer()

speak = wincl.Dispatch("SAPI.SpVoice")
print("Hello I am Veronica, What is your name?")
speak.Speak('Hello I am Verraunikaa, what is your name?')
text = input()


time.sleep(2)
print('I dont talk with you ' + text,)
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak('I dont Talk with you ' + text,)

with sr.Microphone() as source:
    print('Say Something:')
    audio = r.listen(source)
    print ('Done!')

text = r.recognize_google(audio, language = 'IN')

print (text)

text = r.recognize_google(audio, language = 'IN')

time.sleep(2)

if "why" in text:
    print('You tease me everytime')
    speak.Speak('You tease me everytime')
else:
    print("leave it")
    speak.Speak('leave it')
    
time.sleep(3)

with sr.Microphone() as source:
    print('Say Something:')
    audio = r.listen(source)
    print ('Done!')

say = r.recognize_google(audio, language = 'en-us')

print (say)

say = r.recognize_google(audio, language = 'en-us')

if "what" in say:
    print("What are you doing, ")
    speak.speak('What are you doing')
else:
    print("Let me ask you something")
    speak.Speak('Let me ask you something')



time.sleep(4)
print('How is your study going on?')
speak.Speak('How is your study going on')

with sr.Microphone() as source:
    print('Say Something:')
    audio = r.listen(source)
    print ('Done!')

sayy = r.recognize_google(audio, language = 'IN')

print (sayy)

sayy = r.recognize_google(audio, language = 'IN')


if "good" or "fantastic" or "ok" in sayy:
    print("Good to know that")
    speak.Speak('Good to know that')
else:
    print("Kyaa aap bhi!")

time.sleep(5)
print('Now my battery is completely discharged and i am on backup power so let me go and charge myself,,,Bye have a nice day!;')
speak.Speak('Now my battery is completely discharged and i am on backup power mode soo let me go and charge myself bye have a nice day')
