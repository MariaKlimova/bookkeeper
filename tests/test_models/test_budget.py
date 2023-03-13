import pytest

from bookkeeper.repository.memory_repository import MemoryRepository
from bookkeeper.models.budget import Budget


@pytest.fixture
def repo():
    return MemoryRepository()


def test_create_with_full_args_list():
    b = Budget(period='day', limit_maximum=100, category=1, pk=1)
    assert b.period == 'day'
    assert b.limit_maximum == 100
    assert b.category == 1


def test_create_with_no_category():
    b = Budget(period='week', limit_maximum=1000, pk=1)
    assert b.period == 'week'
    assert b.limit_maximum == 1000
    assert b.category == None


def test_can_add_to_repo(repo):
    b = Budget(period='week', limit_maximum=1000)
    pk = repo.add(b)
    assert b.pk == pk
