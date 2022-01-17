import datetime

from Models import User
from User_dao import UserDao
from User_dto import UserDto


def get_single_user(guid: str) -> User:
    user: User = UserDao.get_user_single(guid=guid)
    return user


def create_single_user(user: UserDto) -> bool:
    """
    :param user:
    :return:
    """

    user_old = get_single_user(user.email)

    if not user_old:
        """ oggetto di tipo User """
        new_user = User(
            username=user.username,
            password=user.password,
            email=user.email
        )
        UserDao.create_user_single(new_user)
        return True
    else:
        return False
