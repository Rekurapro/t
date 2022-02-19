import requests
from re import findall
from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def generator():
    return "Hello From Flask!"
