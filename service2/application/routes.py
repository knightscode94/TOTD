from flask import redirect, url_for, jsonify, request
from application import app
import requests, random


def number():
    ans = random.randint(1, 6)

    return ans


@app.route('/get/number', methods=['GET'])
def on_get_request():
    return jsonify(number())


@app.route('/get/animal', methods=['GET'])
def animal():
    response = requests.get('http://api:5000/get/number')
    if response.text == "1":
        return "shark"
    if response.text == "2":
        return "bear"
    if response.text == "3":
        return "fox"
    if response.text == "4":
        return "lion"
    if response.text == "5":
        return "tiger"
    if response.text == "6":
        return "beaver"

    return animal()


@app.route('/sound')
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

    return animal_sounds()
