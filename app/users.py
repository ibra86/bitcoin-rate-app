from dataclasses import dataclass

from flask_login import UserMixin


@dataclass
class User(UserMixin):
    email: str
    password_hsh: str

    def get_id(self):
        return self.email
