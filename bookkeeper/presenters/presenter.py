from typing import Protocol, Callable

from bookkeeper.models.expense import Expense
from bookkeeper.models.category import Category
from bookkeeper.models.budget import Budget

from datetime import datetime

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
        # self.budgetRepo = None
        self.budgetsRepo = SQLiteRepository('test2', Budget)
        self.view = view
        self.expenses = self.expensesRepo.get_all()
        self.categories = self.categoriesRepo.get_all()

        # self.view.register_exp_modifier(self.modify_exp)
        self.view.register_cat_adder(self.add_category)
        self.view.register_cats_getter(self.get_cats)
        self.view.register_exp_adder(self.add_expense)
        self.view.register_exp_getter(self.get_exps)
        self.view.register_budget_updater(self.update_budget)
        self.view.register_budget_getter(self.get_cat_budget)
        self.view.register_sums_getter(self.get_sums)

    def add_category(self, cat: Category) -> None:
        self.categoriesRepo.add(cat)
        all_cats = self.categoriesRepo.get_all()
        self.view.set_cats_list(all_cats)

    def get_cats(self) -> list[Category]:
        # TODO: make it return instances of Category
        return self.categoriesRepo.get_all()

    def add_expense(self, exp: Expense):
        self.expensesRepo.add(exp)
        all_expenses = self.expensesRepo.get_all()
        self.view.set_exp_list(all_expenses)
        self.view.set_sums()

    def get_exps(self) -> list[Expense]:
        # TODO: make it return instances of Expense
        return self.expensesRepo.get_all()

    def update_budget(self, budget: Budget):
        this_budget = list(filter(lambda x: x[3] == budget.category, self.budgetsRepo.get_all()))
        if len(this_budget) > 0:
            budget.pk = this_budget[0][0]
            self.budgetsRepo.update(budget)
        else:
            self.budgetsRepo.add(budget)
        self.view.set_budget()

    def get_cat_budget(self, cat: Category) -> Budget | None:
        all_budgets = list(map(lambda x:
                               Budget(pk=x[0], period=x[1], limit_maximum=x[2], category=x[3]),
                               self.budgetsRepo.get_all()))
        this_budg = list(filter(lambda x: x.category == cat.pk, all_budgets))
        if len(this_budg) > 0:
            return this_budg[0]
        return None

    def get_sums(self, cat: Category | None) -> list[int]:
        raw_list = self.expensesRepo.get_all()
        if cat is not None:
            raw_list = list(filter(lambda x: x[2] == cat.pk, raw_list))
        day_expenses = 0
        week_expenses = 0
        month_expenses = 0
        for record in raw_list:
            amount = record[1]
            date_parts = list(map(int, record[3].split(' ')[0].split('-')))
            date = datetime(date_parts[0], date_parts[1], date_parts[2])
            days_passed = (datetime.now() - date).days
            if days_passed < 1:
                day_expenses += amount
            if days_passed < 7:
                week_expenses += amount
            if days_passed < 31:
                month_expenses += amount
        return [day_expenses, week_expenses, month_expenses]

