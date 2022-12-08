from . import make_fake_BP
from .forms import FakeForm
from .make_fake import MakeFake
from flask import render_template, redirect, url_for, session

@make_fake_BP.route('/', methods=['POST', 'GET'])
def home():
    form = FakeForm()
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        birth = form.birth.data
        email = form.email.data

        session['fake'] = [name, surname, birth, email]
        return redirect(url_for('fake.show_fake'))

    return render_template('make_fake/home.html', form=form)

@make_fake_BP.route('/your_fake')
def show_fake():
    f_session = session.get('fake')
    my_fake = MakeFake(imie=f_session[0], nazw=f_session[1], data_ur=f_session[2], email=f_session[3])
    return render_template('make_fake/show_fake.html', fake=my_fake)
