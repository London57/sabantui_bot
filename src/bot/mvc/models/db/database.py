from dataclasses import dataclass
from .config import *



@dataclass
class QuizTable:
    name: str = table_name
    
    user_id_field: int = user_id_field
    user_username_field: str = user_username_field
    good_answ_field: int = good_answ_field
    bad_answ_field: int = bad_answ_field
    date_field: str = date_field

@dataclass
class QuizDataBase:
    name: str
    table: QuizTable = QuizTable()

