from flask import Blueprint

cryptocurrencies = Blueprint("cryptocurrencies", __name__)

from . import views
