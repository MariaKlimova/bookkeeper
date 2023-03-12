"""Модуль описывает репозиторий, работающий с базой данных"""

from bookkeeper.repository.abstract_repository import AbstractRepository, T
from inspect import get_annotations
import sqlite3
from typing import Any

TYPE_DESCRIPTIONS = {
    "str": "TEXT NOT NULL",
    "int": "INTEGER NOT NULL",
    "float": "REAL NOT NULL"
}
class SQLiteRepository(AbstractRepository[T]):
    """
    Репозиторий, работающий в базе данных SQLite
    """

    def __init__(self, db_file: str, cls: type):
        self.db_file = db_file
        self.table_name = cls.__name__.lower()
        self.fields = get_annotations(cls, eval_str=True)
        self.fields.pop("pk")
        descriptions = [f'{field} {TYPE_DESCRIPTIONS.get(self.fields[field].__name__)}' for field in self.fields]
        create_query = f'CREATE TABLE IF NOT EXISTS {self.table_name}' \
                       f' ({"pk INTEGER NOT NULL PRIMARY KEY,"+ ",".join(descriptions)});'
        with sqlite3.connect(self.db_file) as con:
            cur = con.cursor()
            cur.execute(create_query)
        con.close()

    def add(self, obj: T) -> int:
        names = ', '.join(self.fields.keys())
        p = ', '.join("?"*len(self.fields))
        values = [getattr(obj, x) for x in self.fields]
        with sqlite3.connect(self.db_file) as con:
            cur = con.cursor()
            cur.execute('PRAGMA foreign_keys = ON')
            #s = f'INSERT INTO {self.table_name} ({names}) VALUES ({p})'
            cur.execute(f'INSERT INTO {self.table_name} ({names}) VALUES ({p})', values)
            obj.pk = cur.lastrowid
        con.close()
        return obj.pk

    def get(self, pk: int) -> T | None:
        with sqlite3.connect(self.db_file) as con:
            cur = con.cursor()
            cur.execute(f'SELECT * FROM {self.table_name} WHERE pk = {pk}')
            record = cur.fetchall()
            if len(record) > 0:
                return record[0]

    def update(self, obj: T) -> None:
        pass

    def delete(self, pk: int) -> None:
        pass

    def get_all(self, where: dict[str, Any] | None = None) -> list[T]:
        pass