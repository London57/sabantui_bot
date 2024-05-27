from sqlite3 import (
    connect,
    Cursor
)
from .config import database_name
from .database import DataBase


def connect_db(func):
    def wrapper(*args, **kwargs):
        with connect(database_name) as connection:
            cursor = connection.cursor()
            res = func(cursor=cursor, *args, **kwargs)
            return res
    return wrapper


class WishesRepository:
    def __init__(self, db: DataBase):
        self.db = db

    @connect_db
    def _insert(self, cursor: Cursor, user_id: int, username: str, wishes: str, time: str) -> None:
        cursor.execute(f'''
            INSERT INTO {self.db.table.name}
            ({self.db.table.user_id_field},
             {self.db.table.user_username_field},
             {self.db.table.wishes_field},
             {self.db.table.date_field})
            VALUES (?, ?, ?, ?)
        ''', (user_id, username, wishes, time))

