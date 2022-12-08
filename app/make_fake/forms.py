from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class FakeForm(FlaskForm):
    name = StringField('Wymyśl imię lub pozostaw puste')
    surname = StringField('Wymyśl nazwisko lub pozostaw puste')
    birth = StringField("Wymyśl date urodzenia. 'DD.MM.RRRR'")
    email = StringField("Wymyśl email lub pozostaw puste")
    submit = SubmitField('Stwórz Fejka')