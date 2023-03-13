from typing import Protocol, Callable

from bookkeeper.models.expense import Expense
from bookkeeper.models.category import Category
from bookkeeper.repository.sqlite_repository import SQLiteRepository
from abc import ABC, abstractmethod


# class AbstractView(ABC, Protocol):
#
#
#     def set_expenses_list(self, list[Expense]):
#         pass
#
#     def register_exp_modifier(self, handler: Callable[[Expense], None]):
#         pass
#


class Bookkeeper:
    def __init__(self, view):
        self.expensesRepo = SQLiteRepository('test2', Expense)
        self.categoriesRepo = SQLiteRepository('test2', Category)
        self.view = view
        self.expenses = self.expensesRepo.get_all()
        self.categories = self.categoriesRepo.get_all()

        self.view.register_exp_modifier(self.modify_exp)
        self.view.register_cat_adder(self.add_category)
        self.view.register_cats_getter(self.get_cats)
        self.view.register_exp_adder(self.add_expense)
        self.view.register_exp_getter(self.get_exps)

    def modify_exp(self, exp: Expense) -> None:
        print('bookkeeper modify exp')
        # self.expensesRepo.update(exp)
        # self.view.set_expenses_list(self.expenses)

    def add_category(self, cat: Category) -> None:
        print('add category fired')
        self.categoriesRepo.add(cat)
        all_cats = self.categoriesRepo.get_all()
        self.view.set_cats_list(all_cats)

    def get_cats(self) -> list[Category]:
        return self.categoriesRepo.get_all()

    def add_expense(self, exp: Expense):
        self.expensesRepo.add(exp)
        all_expenses = self.expensesRepo.get_all()
        self.view.set_exp_list(all_expenses)

    def get_exps(self) -> list[Expense]:
        return self.expensesRepo.get_all()

