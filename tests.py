import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2 # исправил метод, потому что стучался в несуществующий метод

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

# чекнул добавление 2-х книг c параметризацией, негативный сценарий
    @pytest.mark.parametrize('book', ['', '12345678901234567890123456789012345678900'])
    def test_add_new_book_add_two_not_valid_name_book(self, exemplar_bookcollector, book):
        exemplar_bookcollector.add_new_book(book)
        assert len(exemplar_bookcollector.get_books_genre()) == 0


    # чекнул наличие книги в списке
    def test_add_new_book_books_name_in_books_genre(self, exemplar_bookcollector):
        exemplar_bookcollector.add_new_book('Отель')
        exemplar_bookcollector.add_new_book('Аэропорт')
        exemplar_bookcollector.add_new_book('Вий')
        assert 'Отель' in exemplar_bookcollector.get_books_genre()


    # устанавливаем книге жанр
    def test_set_book_genre_added_book(self, exemplar_bookcollector):
        exemplar_bookcollector.add_new_book('Вий')
        exemplar_bookcollector.set_book_genre('Вий', 'Ужасы')
        assert exemplar_bookcollector.get_book_genre("Вий") == 'Ужасы'


    # получаем жанр книги по её имени
    def test_get_book_genre_get_specific_book_genre(self, exemplar_bookcollector):
        exemplar_bookcollector.add_new_book('Вий')
        exemplar_bookcollector.set_book_genre('Вий', 'Ужасы')
        assert exemplar_bookcollector.get_book_genre('Вий') == 'Ужасы'


    #Проверка списка книг по выбранному жанру
    def test_get_book_with_specific_genre(self, exemplar_bookcollector):
        exemplar_bookcollector.add_new_book('Отель')
        exemplar_bookcollector.add_new_book('Аэропорт')
        exemplar_bookcollector.add_new_book('Вий')
        exemplar_bookcollector.set_book_genre('Отель', 'Детективы')
        exemplar_bookcollector.set_book_genre('Аэропорт', 'Детективы')
        exemplar_bookcollector.set_book_genre('Вий', 'Ужасы')
        assert exemplar_bookcollector.get_books_with_specific_genre('Детективы') == ['Отель', 'Аэропорт']


    #Проверка книг, подходящих для детей
    def test_get_books_for_children(self, exemplar_bookcollector):
        exemplar_bookcollector.add_new_book('Незнайка')
        exemplar_bookcollector.add_new_book('Атлантида')
        exemplar_bookcollector.add_new_book('Вий')
        exemplar_bookcollector.set_book_genre('Незнайка', 'Мультфильмы')
        exemplar_bookcollector.set_book_genre('Атлантида', 'Фантастика')
        exemplar_bookcollector.set_book_genre('Вий', 'Ужасы')
        assert 'Вий' not in exemplar_bookcollector.get_books_for_children()


    #Добавляем книгу в избранное
    def test_add_book_in_favourites(self, exemplar_bookcollector):
            exemplar_bookcollector.add_new_book('Отель')
            exemplar_bookcollector.add_book_in_favorites('Отель')
            exemplar_bookcollector.add_book_in_favorites('Отель')
            assert 'Отель' in exemplar_bookcollector.get_list_of_favorites_books() and \
                   len(exemplar_bookcollector.get_list_of_favorites_books()) == 1


    #даление книги из избранного
    def test_delete_book_from_favourites(self, exemplar_bookcollector):
            exemplar_bookcollector.add_new_book('Отель')
            exemplar_bookcollector.add_book_in_favorites('Отель')
            exemplar_bookcollector.delete_book_from_favorites('Отель')
            assert len(exemplar_bookcollector.get_list_of_favorites_books()) == 0