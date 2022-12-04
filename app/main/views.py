from . import main_BP
from flask import render_template

@main_BP.route('/')
def home():
    return render_template('home.html')