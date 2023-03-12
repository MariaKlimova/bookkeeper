"""
    Модель бюджета, выеленного на категорию
"""

from dataclasses import dataclass

@dataclass
class Budget:
    """
        Бюджет, установленный на расходы определенной категории за период
        period - период (день, неделя или год)
        limit - ограничение на расходы
        category - категория
        pk - id записи в базе данных

    """
    period: str
    limit: int
    category: int | None = None
    pk: int = 0
