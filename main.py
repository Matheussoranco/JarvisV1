import pyttsx3
import speech_recognition as spr
import requests
from decouple import config
from datetime import datetime
from random import choice
from utils import opening_texts
from functions.os_funcs import open_discord, open_firefox, open_notepad, open_spotify, open_Thunderbird, open_terminal, open_VSCode
from functions.online_funcs import search_google, play_youtube, search_on_wikipedia, send_wpp_message,tell_me_a_joke, get_random_advice



USERNAME = config('USER')
BOTNAME = config('BOTNAME')


engine = pyttsx3.init('espeak')


engine.setProperty('rate', 160)


engine.setProperty('volume', 1.0)


voice = engine.getProperty('voices')
engine.setProperty('voice', voice[7].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = datetime.now().hour
    if(hour>=6) and (hour<=12):
        speak(f"Bom dia senhor")
    elif(hour>=12) and(hour>=16):
        speak(f"Boa tarde senhor")
    elif(hour >= 16) and (hour<19):
        speak(f"Boa noite senhor")
    speak(f"Eu sou {BOTNAME}. Como posso ajudar?")

def take_imput():
    r=spr.Recognizer()
    with spr.Microphone() as source:
        print('Ouvindo...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Ouvindo....')
        query =r.recognize_google (audio, language='pt')
        if not 'exit' in query or 'stop' in query:
             speak(choice(opening_texts))
        else:
            hour = datetime.now().hour
            if hour >= 19 and hour<6:
                speak("Boa Noite senhor")
            else:
                speak("Tenha um bom dia senhor!")
            exit()
    except Exception:
        speak("Desculpe senhor, não entendi.")
        query = 'None'
    return query

if __name__=='__main__':
    greet_user()
    while True:
        query = take_imput().lower()

        if'abra o notepad' in query or 'abra o notepad jarvis' in query:
            open_notepad()

        elif'abra o discord' in query or 'abra o discord jarvis' in query:
            open_discord()

        elif'abra o firefox' in query or 'abra o navegador' in query or 'abra o firefox jarvis' in query or 'abra o navegador jarvis' in query:
            open_firefox()

        elif'abra o terminal' in query or 'abra o terminal jarvis' in query:
            open_terminal()

        elif'abra o vscode' in query or 'abra o visual studio' in query or 'abra o vscode jarvis' in query or 'abra o visual studio jarvis' in query:
            open_VSCode()

        elif'abra o spotify' in query or 'abra o spotify jarvis' in query:
            open_spotify()


        elif'abra o thunderbird' in query or 'Meus emails, Jarvis' in query:
            open_Thunderbird()

        elif'wikipedia' in query or 'wikipedia jarvis' in query:
            speak('O que você quer pesquisar na wikipedia, senhor?')
            search_query = take_imput().lower()
            results = search_on_wikipedia(search_query)
            speak(f"De acordo com a wkipedia, senhor, {results}")
            speak("Para sua conveniência, estou colocando na tela, senhor.")
            print(results)

        #elif'youtube' in query or 'youtube jarvis' in query:
            #speak('O que você quer pesquisar no youtube, senhor?')
            #query = take_imput().lower()
            #play_youtube(video)

        elif'pesquisa no google' in query or 'pesquisa no google, jarvis' in query:
            speak('O que você quer pesquisar no Google, senhor?')
            query = take_imput().lower()
            search_google(query)

        elif'Me conta uma piada' in query or 'me conta uma piada, jarvis' in query:
            speak(f"Essa é boa senhor")
            joke = tell_me_a_joke()
            speak(joke)
            print(joke)

        elif'Jarvis, mande uma mensagem' in query:
            speak('Para qual número, senhor? Por favor, digite')
            number = input("Digite o número: ")
            speak("Qual a mensagem, senhor?")
            message = take_imput().lower()
            send_wpp_message(number, message)
            speak("Eu enviei a mensagem senhor.")

        elif"Jarvis, me dê um conselho" in query:
            speak(f"Não sou o melhor para isso, mas aqui está um conselho, senhor")
            advice = get_random_advice()
            speak(advice)
            print(advice)