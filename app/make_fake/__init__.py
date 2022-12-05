from flask import Blueprint

make_fake_BP = Blueprint('fake', __name__)
from . import views