"""Модуль описывает репозиторий, работающий с базой данных"""
from typing import Any
import sqlite3
from inspect import get_annotations
from bookkeeper.repository.abstract_repository import AbstractRepository, T

TYPE_DESCRIPTIONS = {
    "str": "TEXT NOT NULL",
    "int": "INTEGER NOT NULL",
    "float": "REAL NOT NULL",
    "datetime": "TIMESTAMP"
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
        descriptions = []
        for field in self.fields:
            if self.fields[field].__class__ == type:
                descriptions.append(f'{field} {TYPE_DESCRIPTIONS.get(self.fields[field].__name__)}')
            else:
                if field == "parent":
                    descriptions.append(f'{field} INTEGER')
        # descriptions = \
        #     [f'{field} {TYPE_DESCRIPTIONS.get(self.fields[field].__name__)}'
        #      for field in self.fields]
        create_query = f'CREATE TABLE IF NOT EXISTS {self.table_name}' \
                       f' ({"pk INTEGER NOT NULL PRIMARY KEY," + ",".join(descriptions)});'
        with sqlite3.connect(self.db_file) as con:
            cur = con.cursor()
            cur.execute(create_query)
        con.close()

    def add(self, obj: T) -> int:
        names = ', '.join(self.fields.keys())
        places = ', '.join("?" * len(self.fields))
        values = [getattr(obj, x) for x in self.fields]
        with sqlite3.connect(self.db_file) as con:
            cur = con.cursor()
            cur.execute('PRAGMA foreign_keys = ON')
            # s = f'INSERT INTO {self.table_name} ({names}) VALUES ({p})'
            cur.execute(f'INSERT INTO {self.table_name} ({names}) VALUES ({places})', values)
            if cur.lastrowid:
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
            return None

    def update(self, obj: T) -> None:
        names = self.fields.keys()
        # p = ', '.join("?" * len(self.fields))
        # values = [getattr(obj, x) for x in self.fields]
        with sqlite3.connect(self.db_file) as con:
            cur = con.cursor()
            # cur.execute('PRAGMA foreign_keys = ON')
            new_values = [f'{name} = "{getattr(obj, name)}"' for name in names]
            upd_query = f'UPDATE {self.table_name} ' \
                        f'SET {", ".join(new_values)}' \
                        f' WHERE pk = {obj.pk}'
            # print(upd_query)
            cur.execute(upd_query)
        con.close()

    def delete(self, pk: int) -> None:
        with sqlite3.connect(self.db_file) as con:
            cur = con.cursor()
            cur.execute(f'DELETE FROM {self.table_name} WHERE pk = {pk}')
        con.close()

    def get_all(self) -> list[T]:
        with sqlite3.connect(self.db_file) as con:
            cur = con.cursor()
            cur.execute(f'SELECT * FROM {self.table_name}')
            result = cur.fetchall()

        con.close()
        return result
