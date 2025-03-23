import pytest
from main import BooksCollector


@pytest.fixture(scope="function")
def collector():
    return BooksCollector()


def test_add_new_book_add_only_once(collector):
    collector.add_new_book('Предубеждение и предубеждение')
    collector.add_new_book('Предубеждение и предубеждение')
    assert len(collector.get_books_genre()) == 1


def test_add_new_book_valid_name(collector):
    collector.add_new_book('Гордость и предубеждение')
    assert 'Гордость и предубеждение' in collector.get_books_genre()


def test_add_new_book_empty_name(collector):
    collector.add_new_book('')
    assert '' not in collector.get_books_genre()


def test_add_new_book_longer_40_name(collector):
    collector.add_new_book('Гордость и предубеждение и Предубеждение и Гордость')
    assert 'Гордость и предубеждение и Предубеждение и Гордость' not in collector.get_books_genre()


def test_set_book_genre_and_get_book_genre(collector):
    collector.add_new_book('Гордость и предубеждение - 2')
    collector.set_book_genre('Гордость и предубеждение - 2', 'Комедии')
    assert collector.get_book_genre('Гордость и предубеждение - 2') == 'Комедии'


@pytest.mark.parametrize('book_genre,save_books', [('Фантастика', ['Гордость']),
    ('Ужасы', ['Предубеждение']),
    ('Детективы', ['Дневник Бриджит Джонс']),
])
def test_get_books_with_specific_genre(collector, book_genre,save_books):
    collector.add_new_book('Гордость')
    collector.set_book_genre('Гордость', 'Фантастика')
    collector.add_new_book('Предубеждение')
    collector.set_book_genre('Предубеждение', 'Ужасы')
    collector.add_new_book('Дневник Бриджит Джонс')
    collector.set_book_genre('Дневник Бриджит Джонс', 'Детективы')
    assert collector.get_books_with_specific_genre(book_genre) == save_books


def test_get_books_for_children(collector):
    collector.add_new_book('Гордость')
    collector.set_book_genre('Гордость', 'Фантастика')
    collector.add_new_book('Предубеждение')
    collector.set_book_genre('Предубеждение', 'Ужасы')
    collector.add_new_book('Дневник Бриджит Джонс')
    collector.set_book_genre('Дневник Бриджит Джонс', 'Детективы')
    collector.add_new_book('Незнайка на луне')
    collector.set_book_genre('Незнайка на луне', 'Мультфильмы')
    collector.add_new_book('12 стульев')
    collector.set_book_genre('12 стульев', 'Комедии')
    assert collector.get_books_for_children() == ['Гордость', 'Незнайка на луне', '12 стульев']


def test_add_book_in_favorites(collector):
    collector.add_new_book('Дневник Бриджит Джонс 2')
    collector.add_book_in_favorites('Дневник Бриджит Джонс 2')
    assert 'Дневник Бриджит Джонс 2' in collector.get_list_of_favorites_books()


def test_delete_book_from_favorites(collector):
    collector.add_new_book('Дневник Бриджит Джонс 2')
    collector.add_book_in_favorites('Дневник Бриджит Джонс 2')
    collector.delete_book_from_favorites('Дневник Бриджит Джонс 2')
    assert 'Дневник Бриджит Джонс 2' not in collector.get_list_of_favorites_books()


def test_get_list_of_favorites_books(collector):
    collector.add_new_book('Дневник Бриджит Джонс 3')
    collector.add_book_in_favorites('Дневник Бриджит Джонс 3')
    assert collector.get_list_of_favorites_books() == ['Дневник Бриджит Джонс 3']


def test_get_books_genre(collector):
    collector.add_new_book('Незнайка на луне')
    collector.set_book_genre('Незнайка на луне', 'Мультфильмы')
    assert collector.get_books_genre() == {'Незнайка на луне': 'Мультфильмы'}


def test_set_book_genre_unknown_genre(collector):
    collector.add_new_book('Страна Оз')
    collector.set_book_genre('Страна Оз', 'Криминал')
    assert collector.get_book_genre('Страна Оз') not in collector.genre
    assert collector.get_book_genre('Страна Оз') == ''


def test_add_book_in_favorites_not_in_collection(collector):
    collector.add_book_in_favorites('Капитанская дочка')
    assert 'Капитанская дочка' not in collector.get_list_of_favorites_books()