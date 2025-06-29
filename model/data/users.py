import dataclasses


@dataclasses.dataclass
class User:
    username: str
    email: str
    password: str
    invalid_password: str


user = User(username="shikhalas", email="sh.shikhalas+2@gmail.com",
            password="?Mz?H9QU8WJ@ydp", invalid_password="Mz?H9QU8WJ@ydp")
