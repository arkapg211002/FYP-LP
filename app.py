import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='.')
app.secret_key = os.environ.get("SESSION_SECRET")

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)
