from flask import Blueprint, render_template, request, redirect
from .generator import AI

generator = Blueprint('generator',__name__)

@generator.route('/')
def index():
    return render_template('index.html')

@generator.route('/analyze',methods=['POST'])
def analyze():
    title = request.form["title"]
    text = AI.generate_text(title)

    return render_template('index.html', text=text)