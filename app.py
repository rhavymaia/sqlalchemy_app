from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# postgresql://username:password@localhost:5432/your_database
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://pweb:123456@localhost:5432/aemotor"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)


class Usuario(db.Model):
    __tablename__ = "tb_usuario"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    nascimento = db.Column(db.Date, nullable=True)
    created = db.Column(db.Date, nullable=True)

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User %r>' % self.username

    def __add__(self, other):
        return User(self.username + other.username)

    # user1 = User("Marcella")
    # user2 = User("Mateus")
    # resultado = 1 + 1 + 1
    # pessoaResultado = user1 + user2 + user3


class Endereco(db.Model):
    __tablename__ = "tb_endereco"

    id = db.Column(db.Integer, primary_key=True)
    logradouro = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Address %r>' % self.logradouro


class Prefeitura(db.Model):
    __tablename__ = "tb_prefeitura"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<Prefeitura %r>' % self.email
