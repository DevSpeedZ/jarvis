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

#abrir um jogo da steam
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
            return ""

#loop principal
while True:
    if keyboard.is_pressed('home'):
        print('escutando...')
        comando = unidecode(mic().lower()) # unidecode tira o acento e .lower() tira letra maiuscula

        #abrir marvel rival
        if 'marvel' in comando:
            falar('abrindo marvel rivals')
            print('abrindo marvel rivals')
            steamgame(2767030)
        
        #modo transcrição
        if 'transcricao' in comando:
            falar('ativando modo de transcrição')
            while True:
                comando = unidecode(mic().lower())
                keyboard.write(comando + " ")
                if 'desativar' in comando:
                    break
#
#tudo que eu falar agora quero que saia alias por favor saia da minha frente pois estou tentando passar tu ta com um chat da cristovao  
#fazer a transcrição de voz para texto
#quando ouvir a palavra descrição entrar em um loop
#onde tudo q falado é digitado
#ao apertar o end o loop é quebrado


