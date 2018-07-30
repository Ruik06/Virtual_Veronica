import win32com.client as wincl
import time
import random

speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak('Hello I am Verraunikaaa, what is your name?')
name = input(str("Hello I am Veronica, what is your name? "))


time.sleep(2)
print("Kya " + name,'me apse baat nahi kr rahi')

feeling = input("")

time.sleep(2)

if "kyu" in feeling:
    print('kitna chidhate aap muze')
else:
    print("chodo")
    
time.sleep(3)

say = input("")

if "kya" in say:
    print("chodo aap batao, ")
else:
    print("Study karo")

sayy = input("")

time.sleep(4)

if "ok" in sayy:
    print("bye!")
    quit()

else:
    print("Kyaa aap bhi!")

time.sleep(5)
favcolour = input("What is your favourite colour? ")

colours = ["Red","Green","Blue"]

time.sleep(2)
print("My favourite colour is " + random.choice(colours))
