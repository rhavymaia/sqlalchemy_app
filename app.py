from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    nascimento = db.Column(db.Date, nullable=True)
    created = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    logradouro = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Address %r>' % self.logradouro
