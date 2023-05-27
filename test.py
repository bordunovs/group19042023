import pytest
from library import miles_to_kilometers, get_unique_sorted_elements

def test_miles_to_kilometers_positive():
    assert miles_to_kilometers(10) == 16.0934


def test_miles_to_kilometers_zero():
    assert miles_to_kilometers(0) == 0


def test_miles_to_kilometers_negative():
    with pytest.raises(ValueError):
        miles_to_kilometers(-5)


def test_miles_to_kilometers_float():
    assert miles_to_kilometers(3.5) == 5.63269


def test_miles_to_kilometers_large_value():
    assert miles_to_kilometers(100000) == 160934


# Тести для другої функції get_unique_sorted_elements:
def test_get_unique_sorted_elements_list():
    assert get_unique_sorted_elements([3, 2, 1, 2, 3, 4]) == (1, 2, 3, 4)


def test_get_unique_sorted_elements_set():
    assert get_unique_sorted_elements({3, 2, 1, 2, 3, 4}) == (1, 2, 3, 4)


def test_get_unique_sorted_elements_string():
    assert get_unique_sorted_elements("hello") == ('e', 'h', 'l', 'o')


def test_get_unique_sorted_elements_dict():
    assert get_unique_sorted_elements({'a': 1, 'b': 2, 'c': 3}) == ('a', 'b', 'c')


def test_get_unique_sorted_elements_empty():
    assert get_unique_sorted_elements([]) == ()
if __name__ == '__main__':
    pytest.main()


