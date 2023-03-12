from bookkeeper.repository.sqlite_repository import SQLiteRepository

import pytest
from inspect import get_annotations

@pytest.fixture
def custom_class():
    class Custom:
        pk: int = 0
        value: str = f'HELLO {pk}'

    return Custom


@pytest.fixture
def repo(custom_class):
    return SQLiteRepository("test1", custom_class)


def test_crud(repo, custom_class):
    #pass
    obj = custom_class()
    pk = repo.add(obj)
    assert obj.pk == pk
    foundRecord = repo.get(pk)
    assert foundRecord[0] == obj.pk
    assert foundRecord[1] == obj.value
    # obj2 = custom_class()
    # obj2.pk = pk
    # repo.update(obj2)
    # assert repo.get(pk) == obj2
    # repo.delete(pk)
    # assert repo.get(pk) is None
