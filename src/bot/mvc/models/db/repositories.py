from datetime import datetime
import sqlite3
from .config import database_name
from .database import DataBase


def connect_db(func):
    def wrapper(*args, **kwargs):
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            res = func(cursor=cursor, *args, **kwargs)
            return res
    return wrapper

def replace_select_data(data: tuple):
    return str(data).replace("('",'').replace("',)", '')

            
class QuizRepository:
    def __init__(self, db: DataBase):
        self.db = db
    
    @connect_db
    def _select(self, cursor, user_id: int) -> list:
        cursor.execute(f'''
            SELECT {self.db.table.good_answ_field},
                   {self.db.table.bad_answ_field},
                   {self.db.table.date_field}
            FROM {self.db.table.name}
            WHERE {self.db.table.user_field} == {user_id}
            ORDER BY {self.db.table.date_field} 
        ''')
        data = cursor.fetchall()
        data = [replace_select_data(row) for row in data]
        print(data)
        return data

    @connect_db
    def _insert(self, cursor, user_id: int, good_answ_c: int, bad_answ_c: int, time) -> None:
        # Преобразуем datetime в строку
        # Убедимся, что все передаваемые параметры имеют правильные типы
        user_id = int(user_id)
        good_answ_c = int(good_answ_c)
        bad_answ_c = int(bad_answ_c)
        print(user_id, type(user_id), time, type(time), good_answ_c, type(good_answ_c), bad_answ_c, type(bad_answ_c))
        cursor.execute(f'''
            INSERT INTO {self.db.table.name}
            ({self.db.table.user_field},
             {self.db.table.good_answ_field},
             {self.db.table.bad_answ_field},
             {self.db.table.date_field})
            VALUES (?, ?, ?, ?)
        ''', (user_id, good_answ_c, bad_answ_c, time))

class QuizRepositoryService(QuizRepository):
    def select(self, user_id: int):
        return self._select(user_id=user_id)
    
    def insert(self, user_id: int, good_answ_c: int, bad_anss_c: int, time):
        return self._insert(user_id=user_id, good_answ_c=good_answ_c, bad_answ_c=bad_anss_c, time=time)