from flask import render_template, redirect, url_for
from application import app
import requests

@app.route('/generate_animal',methods=['GET','POST'])
def generate_animal():
    animal = requests.get('http://localhost:5001/get_animal')
    return animal


