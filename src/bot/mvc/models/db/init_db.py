from .config import (
    database_name,
    table_name,
    user_id_field,
    user_username_field,
    good_answ_field,
    bad_answ_field,
    date_field,
)
from sqlite3 import connect
from .database import QuizDataBase


def init_db() -> None:
    query_create_db = (f'''
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    {user_id_field} INTEGER NOT NULL,
                    {user_username_field} TEXT NOT NULL UNIQUE,
                    {good_answ_field} INTEGER NOT NULL,
                    {bad_answ_field} INTEGER NOT NULL,
                    {date_field} TIMESTAMP)
            ''')
    
    with connect(database_name) as connection:
        cursor = connection.cursor()
        cursor.execute(query_create_db)
        connection.commit()


def create_quiz_db_model() -> QuizDataBase:
    return QuizDataBase(
        database_name,
    )