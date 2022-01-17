from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'fwefew32323432wfwgferge!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:rootadmin@localhost/testdb'

# manager = Manager(app)
db = SQLAlchemy(app)
flask_bcrypt = Bcrypt(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    created_on = db.Column(db.DateTime(), default=datetime.now().date(), nullable=False)
    expiration_on = db.Column(db.DateTime(), default=datetime.now().date() + timedelta(days=30), nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = flask_bcrypt.generate_password_hash(password).decode('utf-8')
        self.email = email

    @property
    def password_hash(self):
        raise AttributeError('password: write-only field')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password, password)

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.username)


# db.drop_all()

# db.create_all()
# db.session.commit()

CORS(app)
