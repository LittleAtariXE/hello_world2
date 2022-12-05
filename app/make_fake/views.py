from . import make_fake_BP
from flask import render_template

@make_fake_BP.route('/')
def home():
    return render_template('make_fake/home.html')