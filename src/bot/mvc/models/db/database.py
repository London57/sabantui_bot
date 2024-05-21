from dataclasses import dataclass
from .config import *



@dataclass
class Table:
    name: str = table_name
    user_field: int = user_field
    good_answ_field: int = good_answ_field
    bad_answ_field: int = bad_answ_field
    date_field: str = date_field

@dataclass
class DataBase:
    name: str
    table: Table = Table()

