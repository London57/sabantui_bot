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


class QuizRepository:
    def __init__(self, db: DataBase):
        self.db = db
    
    @connect_db
    def _select(self, cursor: Cursor):
        cursor.execute(f'''
            SELECT {self.db.table.user_username_field},
            {self.db.table.good_answ_field} 
            {self.db.table.date_field}
            FROM {self.db.table.name}
            ORDER BY {self.db.table.good_answ_field}, {self.db.table.date_field}
        ''')
        data = cursor.fetchall()
        return self.select_leaders_list(data)
    
    def select_leaders_list(self, l):
        r_l = []
        for i in l:
            r_l.append([*i])
            print(i, *i)
        for i in r_l:
            print(i)

        print(r_l)
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
        print('insert')

    @connect_db
    def _check_quiz(self, cursor: Cursor, user_id: int):
        cursor.execute(f"""
            SELECT {self.db.table.user_id_field}
            FROM {self.db.table.name}
            WHERE {self.db.table.user_id_field} == {user_id}
        """)
        
        data = cursor.fetchall()
        return self.get_select_data(data)

    def get_select_data(self, data):
        print([self.replace_select_data(row) for row in data])
        return [self.replace_select_data(row) for row in data]

    def replace_select_data(self, data: tuple):
        return str(data).replace("('",'').replace("',)", '')


class QuizRepositoryService(QuizRepository):
    def select(self) -> list:
        return self._select()
    
    def insert(self, user_id: int, username: str, good_answ_c: int, bad_anss_c: int, time):
        return self._insert(user_id=user_id, username=username, good_answ_c=good_answ_c, bad_answ_c=bad_anss_c, time=time)
    
    def check_quiz(self, user_id: int):
        return self._check_quiz(user_id=user_id)