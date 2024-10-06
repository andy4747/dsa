from src.algorithms.sorting import bubble_sort
from src.algorithms.searching import linear_search

def test_bubble_sort():
    assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]

def test_linear_search():
    assert linear_search([1, 3, 5, 7, 9], 5) == 2
    assert linear_search([1, 3, 5, 7, 9], 1) == 0
    assert linear_search([1, 3, 5, 7, 9], 9) == 4
    assert linear_search([1, 3, 5, 7, 9], 4) == -1
    assert linear_search([], 1) == -1
