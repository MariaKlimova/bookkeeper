"""Модуль описывает репозиторий, работающий с базой данных"""

from bookkeeper.repository.abstract_repository import AbstractRepository, T
class SQLiteRepository(AbstractRepository[T]):
    """
    Репозиторий, работающий в базе данных SQLite
    """