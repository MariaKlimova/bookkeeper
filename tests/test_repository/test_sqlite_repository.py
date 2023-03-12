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
    obj2 = custom_class()
    obj2.pk = obj.pk
    obj2.value = "Some other value"
    repo.update(obj2)
    foundRecord = repo.get(obj2.pk)
    assert foundRecord[0] == obj2.pk
    assert foundRecord[1] == obj2.value
    repo.delete(pk)
    assert repo.get(pk) is None
