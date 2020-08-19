from flask import redirect, url_for, jsonify, request
from application import app
import requests, random



@app.route('/get/animal', methods=['GET'])
def get_animal():
    animals=["shark","bear","fox","lion","tiger","beaver"]
    animal = animals[random.randrange(6)]
    return Response(animal,mimetype='text/plain')


@app.route('/get/sound', methods=['GET'])
def animal_sounds():
    response = requests.get('http://api:5000/get/animal')
    if response.text == "lion" or response.text == "tiger":
        return "Rawr"
    if response.text == "bear":
        return "Grrr"
    if response.text == "shark":
        return "duunnn dunn... duuuunnnn duun... duuunnnnnnnn dun dun dun dun dun dun dun dun dun dun dunnnnnnnnnnn dunnnn"
    if response.text == "fox":
        return "But what does the fox say?"
    if response.text == "beaver":
        return "nom nom nom nom nom nom"

    return Response(animal_sounds,mimetype='text/plain')
