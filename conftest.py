import pytest

from main import BooksCollector

@pytest.fixture() # фикстура, которая создает объект класса BookCollector
def exemplar_bookcollector():
    collector = BooksCollector()
    return collector