from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application
app = Flask(__name__)
# Set  configuration variable for flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:database@localhost:54321/example'

# create new instance of the class
db = SQLAlchemy(app)


class Person(db.Model):
    #__tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

# db.create detects models and creates table for us
db.create_all()


@app.route('/')
def index():
    return 'Hello World!'
