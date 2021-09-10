import serial
import time
import keyboard
import speech_recognition as sr

recognizer = sr.Recognizer()
adata = serial.Serial('com7',baudrate=9600, timeout=1)
def LEDB():
   adata.write(b'b')
   print(adata)

def LEDNB():
    adata.write(b'n')
    print(adata)

def LEDR():
   adata.write(b'r')
   print(adata)

def LEDNR():
    adata.write(b't')
    print(adata)

def LEDG():
   adata.write(b'l')
   print(adata)

def LEDNG():
    adata.write(b'x')
    print(adata)

def LEDY():
   adata.write(b'g')
   print(adata)

def LEDNY():
    adata.write(b'c')
    print(adata)

while 1:
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(query)

            if query == 'red':
                LEDR()

            if query == 'blue':
                LEDB()

            if query == 'yellow':
                LEDY()

            if query == 'Green':
                LEDG()

            if query == 'off':

                LEDNB()
                LEDNY()
                LEDNG()
                LEDNR()


            if query == 'computer':

                LEDNB()
                LEDNY()
                LEDNG()
                LEDNR()


        except sr.UnknownValueError:
            print("Could not understand audio")
            print('Sucker')


