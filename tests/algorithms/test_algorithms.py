import pytest
from src.algorithms import bubble_sort
from src.algorithms import linear_search
from src.algorithms import MTBArray

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


def test_insert_at_last():
    """Test various scenarios for inserting a value at the end of a list."""
    mtb_array = MTBArray()

    # Test 1: Inserting into a normal list
    nums = [1, 2, 3]
    mtb_array.insert_at_last(nums, 4)
    assert nums == [1, 2, 3, 4], "The list should be [1, 2, 3, 4] after insertion."

    # Test 2: Inserting into an empty list
    nums = []
    mtb_array.insert_at_last(nums, 1)
    assert nums == [1], "The list should be [1] after inserting into an empty list."

    # Test 3: Inserting multiple values sequentially
    nums = [5, 10]
    mtb_array.insert_at_last(nums, 15)
    mtb_array.insert_at_last(nums, 20)
    assert nums == [5, 10, 15, 20], "The list should be [5, 10, 15, 20] after multiple insertions."

    # Test 4: Inserting a large value
    nums = [1, 2, 3]
    mtb_array.insert_at_last(nums, 1000000)
    assert nums == [1, 2, 3, 1000000], "The list should contain the large value at the end."

    # Test 5: Inserting negative value
    nums = [10, 20, 30]
    mtb_array.insert_at_last(nums, -5)
    assert nums == [10, 20, 30, -5], "The list should contain the negative value at the end."

    # Test 6: Inserting zero
    nums = [1, 2, 3]
    mtb_array.insert_at_last(nums, 0)
    assert nums == [1, 2, 3, 0], "The list should contain zero at the end."


def test_insert_at_first():
    """Test various scenarios for inserting a value at the beginning of a list."""
    mtb_array = MTBArray()

    # Test 1: Inserting into a normal list
    nums = [2, 3, 4]
    mtb_array.insert_at_first(nums, 1)
    assert nums == [1, 2, 3, 4], "The list should be [1, 2, 3, 4] after insertion."

    # Test 2: Inserting into an empty list
    nums = []
    mtb_array.insert_at_first(nums, 5)
    assert nums == [5], "The list should be [5] after inserting into an empty list."

    # Test 3: Inserting multiple values sequentially
    nums = [6, 7]
    mtb_array.insert_at_first(nums, 5)
    mtb_array.insert_at_first(nums, 4)
    assert nums == [4, 5, 6, 7], "The list should be [4, 5, 6, 7] after multiple insertions."

    # Test 4: Inserting a negative value
    nums = [1, 2, 3]
    mtb_array.insert_at_first(nums, -1)
    assert nums == [-1, 1, 2, 3], "The list should contain the negative value at the beginning."

    # Test 5: Inserting zero
    nums = [10, 20, 30]
    mtb_array.insert_at_first(nums, 0)
    assert nums == [0, 10, 20, 30], "The list should contain zero at the beginning."

def test_insert_at():
    """Test various scenarios for inserting a value at a specified index in a list."""
    mtb_array = MTBArray()

    # Test 1: Inserting at the beginning of the list
    nums = [2, 3, 4]
    mtb_array.insert_at(nums, 0, 1)
    assert nums == [1, 2, 3, 4], "The list should be [1, 2, 3, 4] after insertion at the beginning."

    # Test 2: Inserting at the end of the list
    nums = [1, 2, 3]
    mtb_array.insert_at(nums, 3, 4)
    assert nums == [1, 2, 3, 4], "The list should be [1, 2, 3, 4] after insertion at the end."

    # Test 3: Inserting in the middle of the list
    nums = [1, 2, 4]
    mtb_array.insert_at(nums, 2, 3)
    assert nums == [1, 2, 3, 4], "The list should be [1, 2, 3, 4] after insertion in the middle."

    # Test 4: Inserting into an empty list
    nums = []
    mtb_array.insert_at(nums, 0, 1)
    assert nums == [1], "The list should be [1] after inserting into an empty list."

    # Test 5: Inserting at an invalid index (too high)
    nums = [1, 2, 3]
    with pytest.raises(IndexError):
        mtb_array.insert_at(nums, 5, 10)

    # Test 6: Inserting at a negative index
    nums = [1, 2, 3]
    with pytest.raises(IndexError):
        mtb_array.insert_at(nums, -1, 0)


def test_remove_from_first():
    obj = MTBArray()

    # Test case 1: Remove element at index 2
    nums = [1, 2, 3, 4, 5]
    index = 2
    obj.remove_from_first(nums, index)
    expected = [1, 2, 4, 5]
    assert nums == expected, f"Expected {expected} after removing index {index}, but got {nums}."
    print(f"Test passed for index {index}: List correctly updated to {nums}.")

    # Test case 2: Index is out of bounds (positive)
    nums = [1, 2, 3]
    index = 5
    with pytest.raises(IndexError):
        obj.remove_from_first(nums, index)
    print(f"Test passed for out-of-bounds index {index}: IndexError was raised as expected.")

    # Test case 3: Negative index (assuming negative indices should raise IndexError)
    nums = [1, 2, 3, 4]
    index = -1
    with pytest.raises(IndexError):
        obj.remove_from_first(nums, index)
    print(f"Test passed for negative index {index}: IndexError was raised as expected.")


def test_remove_at():
    obj = MTBArray()
    # Test case 1: Remove element at index 2
    nums = [1, 2, 3, 4, 5]
    index = 2
    obj.remove_at(nums, index)
    expected = [1, 2, 4, 5]
    assert nums == expected, f"Expected {expected} after removing element at index {index}, but got {nums}."
    print(f"Test passed for index {index}: List correctly updated to {nums}.")

    # Test case 2: Index is out of bounds (positive)
    nums = [1, 2, 3]
    index = 5
    with pytest.raises(IndexError):
        obj.remove_at(nums, index)
    print(f"Test passed for out-of-bounds index {index}: IndexError was raised as expected.")

    # Test case 3: Negative index (assuming negative indices should raise IndexError)
    nums = [1, 2, 3, 4]
    index = -1
    with pytest.raises(IndexError):
        obj.remove_at(nums, index)
    print(f"Test passed for negative index {index}: IndexError was raised as expected.")

    # Test case 4: Remove the first element
    nums = [10, 20, 30, 40]
    index = 0
    obj.remove_at(nums, index)
    expected = [20, 30, 40]
    assert nums == expected, f"Expected {expected} after removing element at index {index}, but got {nums}."
    print(f"Test passed for index {index}: List correctly updated to {nums}.")

    # Test case 5: Remove the last element
    nums = [10, 20, 30, 40]
    index = 3
    obj.remove_at(nums, index)
    expected = [10, 20, 30]
    assert nums == expected, f"Expected {expected} after removing element at index {index}, but got {nums}."
    print(f"Test passed for index {index}: List correctly updated to {nums}.")
