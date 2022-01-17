import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class UserDto:
    username: str
    email: str
    password: str
    created: datetime
    expiration: datetime

