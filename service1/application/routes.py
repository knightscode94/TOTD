from flask import render_template, redirect, url_for
from application import app
import requests

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', title='Home')

@app.route('/get/animal',methods=['GET','POST'])
def animal():
    animal = requests.get('http://service2:5001/animal/name')
    sound = requests.post('http://service2:5001/animal/sound', data=animal.text)
    return render_template('animals.html', title='Animal', animal = animal.text, sound = sound.text)


