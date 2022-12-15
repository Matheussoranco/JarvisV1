import requests
import wikipedia
import pywhatkit as pykit
from email.message import EmailMessage
import smtplib
from decouple import config

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results

def play_youtube(video):
    pykit.playonyt(video)


def search_google(query):
    pykit.search(query)


def send_wpp_message(number, message):
    pykit.sendwhatmsg_instantly(f"+55{number}", message)


#def send_email(reciever_address, subject, message):

def tell_me_a_joke():
    headers = {
        'accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", header=headers)
    return res["joke"]


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']