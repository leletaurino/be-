from Models import User
from flask_sqlalchemy import BaseQuery, Pagination
from Models import db


class UserDao:
    @staticmethod
    def get_user_single(guid: str):
        try:
            user: BaseQuery = User.query.filter(User.email == guid).one_or_none()
            return user
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def create_user_single(new_user: User):
        try:
            db.session.add(new_user)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise e
