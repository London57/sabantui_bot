from .config import (
    database_name,
    table_name,
    user_id_field,
    user_username_field,
    wishes_field,
    date_field,
)
from sqlite3 import connect
from .database import DataBase


def init_wishes_table() -> None:
    query_create_db = (f'''
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    {user_id_field} INTEGER NOT NULL,
                    {user_username_field} TEXT NOT NULL,
                    {wishes_field} TEXT NOT NULL,
                    {date_field} TIMESTAMP)
            ''')
    
    with connect(database_name) as connection:
        cursor = connection.cursor()
        cursor.execute(query_create_db)
        connection.commit()


def create_wishes_db_model() -> DataBase:
    return DataBase(
        database_name,
    )