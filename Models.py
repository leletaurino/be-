from datetime import datetime, timedelta
# from Server import db


# class User(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer(), primary_key=True)
#     username = db.Column(db.String(45), nullable=False, unique=True)
#     password = db.Column(db.String(255), nullable=False)
#     created_on = db.Column(db.DateTime(), default=datetime.now().date(), nullable=False)
#     expiration_on = db.Column(db.DateTime(), default=datetime.now().date() + timedelta(days=30), nullable=False)
#
#     def __repr__(self):
#         return "<{}:{}>".format(self.id, self.username)