from sqlite3 import (
    connect,
    Cursor
)
from .config import database_name
from .database import QuizDataBase


def connect_db(func):
    def wrapper(*args, **kwargs):
        with connect(database_name) as connection:
            cursor = connection.cursor()
            res = func(cursor=cursor, *args, **kwargs)
            return res
    return wrapper


class QuizRepository:
    def __init__(self, db: QuizDataBase):
        self.db = db
    
    @connect_db
    def _select_leaders_quiz(self, cursor: Cursor):
        cursor.execute(f'''
            SELECT {self.db.table.user_username_field},
            {self.db.table.good_answ_field},
            {self.db.table.date_field}
            FROM {self.db.table.name}
            ORDER BY {self.db.table.good_answ_field}, {self.db.table.date_field} DESC
        ''')
        data = cursor.fetchall()
        result_list = self.select_leaders_list(data)
        result_list.reverse()
        return result_list
    
    def select_leaders_list(self, l):
        r_l = []
        for i in l:
            r_l.append([*i])
        return r_l

    @connect_db
    def _insert(self, cursor: Cursor, user_id: int, username: str, good_answ_c: int, bad_answ_c: int, time: str) -> None:
        cursor.execute(f'''
            INSERT INTO {self.db.table.name}
            ({self.db.table.user_id_field},
             {self.db.table.user_username_field},
             {self.db.table.good_answ_field},
             {self.db.table.bad_answ_field},
             {self.db.table.date_field})
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, username, good_answ_c, bad_answ_c, time))
        print('insert ', username)


    @connect_db
    def _check_quiz(self, cursor: Cursor, user_id: int):
        cursor.execute(f"""
            SELECT {self.db.table.user_username_field},
            {self.db.table.good_answ_field},
            {self.db.table.date_field}
            FROM {self.db.table.name}
            WHERE {self.db.table.user_id_field} == {user_id}
        """)

        data = cursor.fetchall()
        print(data)
        try:
            return list(data[0])
        except IndexError:
            return 0

