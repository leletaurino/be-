from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'fwefew32323432wfwgferge!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:rootadmin@localhost/testdb'

# manager = Manager(app)
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.now().date(), nullable=False)
    expiration_on = db.Column(db.DateTime(), default=datetime.now().date() + timedelta(days=30), nullable=False)

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.username)


db.create_all()
db.session.commit()

CORS(app)