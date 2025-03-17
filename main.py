import speech_recognition as sr
#import datetime
#import pyautogui
import pyttsx3
import keyboard
import subprocess
import time
from unidecode import unidecode

#concatenação
texto_fala = pyttsx3.init() #concatenando o speaker
voices = texto_fala.getProperty('voices') #concatenando as vozes
r = sr.Recognizer() #concatenando o reconhecedor

#sistema de fala
def falar(audio):

    texto_fala.setProperty('voice', voices[0].id)  #setando a voz
    texto_fala.say(audio) #falando
    texto_fala.runAndWait() #esperar

def steamgame(id):
    subprocess.Popen(["C:\\Program Files (x86)\\Steam\\steam.exe", f"steam://run/{id}"])



#reconhecimento do comando
def mic():

    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio =  r.listen(source)

        try:
            print('reconhecendo...')
            comando = r.recognize_google(audio, language='pt-BR')
            print (comando)
            return(comando)
        except Exception as e:
            falar("Repita por favor")
            print(e)
            return "None"

while True:
    if keyboard.is_pressed('home'):
        print('escutando...')
        comando = unidecode(mic().lower()) # unidecode tira o acento e .lower() tira letra maiuscula

        #abrir marvel rival
        if 'marvel' in comando:
            falar('abrindo marvel rivals')
            print('abrindo marvel rivals')
            steamgame(2767030)

#fazer a transcrição de voz para texto

