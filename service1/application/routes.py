from flask import render_template, redirect, url_for
from application import app
import requests

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', title='Home')

@app.route('/generate_animal',methods=['GET','POST'])
def generate_animal():
    animal = requests.get('http://localhost:5001/get/animal')
    sound = requests.post('http://localhost:5001/get/sound', data=animal.text)
    return render_template('animals.html', title='Animal', animal = animal.text, sound = sound.text)


