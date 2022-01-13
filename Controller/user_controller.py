from Models import User
from User_dao import UserDao


def get_single_user(guid: str) -> User:
    user: User = UserDao.get_user_single(guid=guid)
    return user


def create_single_user(user: dict) -> bool:
    # for key, value in user.items():
    """ creare un oggetto di tipo User dal dizionario user """
    resp: bool = UserDao.create_user_single(new_user="passare qui l'oggetto di tipo User")
    return resp