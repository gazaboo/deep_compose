from flask import Flask

app = Flask(__name__)

ibm_url = "http://ibm-summarizer:5000/model/predict"
ibm_url_get = "http://ibm-summarizer:5000/model/metadata"

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

from . import routes
