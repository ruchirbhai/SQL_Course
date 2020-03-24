from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application
app = Flask(__name__)
# Set  configuration variable for flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:database@localhost:5433/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create new instance of the class
db = SQLAlchemy(app)


class Person(db.Model):
    tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    # Create a wrapper functino to display the table in a user friendly way
    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'

# db.create detects models and creates table for us
db.create_all()


@app.route('/')
def index():
    # Querying the name which was added a person name Ruchir manually to the table
    person = Person.query.first()
    return 'Hello ' + person.name + '!'
