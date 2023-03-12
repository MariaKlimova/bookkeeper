"""
    Модель бюджета, выеленного на категорию
"""

from dataclasses import dataclass

@dataclass
class Budget:
    """
        Категория расходов, хранит название в атрибуте name и ссылку (id) на
        родителя (категория, подкатегорией которой является данная) в атрибуте parent.
        У категорий верхнего уровня parent = None
    """
    period: str
    limit: int
    category: int | None = None
    pk: int = 0
