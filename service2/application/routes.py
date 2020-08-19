from flask import request, Response
from application import app
import requests, random


@app.route('/animal/name', methods=['GET'])
def animal_name():
    animals = ["shark", "bear", "fox", "lion", "tiger", "beaver"]
    animal = animals[random.randrange(6)]
    return Response(animal, mimetype='text/plain')


@app.route('/animal/sound', methods=['POST'])
def animal_sound():
    animal = request.data.decode("utf-8")
    if animal == "lion":
        sound = "Rawr"
    elif animal == "tiger":
        sound = "Rawr"
    elif animal == "bear":
        sound = "Grrr"
    elif animal == "shark":
        sound = "duunnn dunn... duuuunnnn duun... duuunnnnnnnn dun dun dun dun dun dun dun dun dun dun dunnnnnnnnnnn dunnnn"
    elif animal == "fox":
        sound = "But what does the fox say?"
    elif animal == "beaver":
        sound = "nom nom nom nom nom nom"
    else:
        sound = "Its mythical"

    return Response(sound, mimetype='text/plain')
