from flask import Flask
# from flask-alchemy import


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'