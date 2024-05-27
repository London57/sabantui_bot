from dataclasses import dataclass
from .config import *



@dataclass
class Table:
    name: str = table_name
    user_id_field: int = user_id_field
    user_username_field: str = user_username_field
    wishes_field: str = wishes_field
    date_field: str = date_field

@dataclass
class DataBase:
    name: str
    table: Table = Table()

