from src.leetcode.easy.array_warmup import ArrayWarmup

def test_max():
    solution = ArrayWarmup()
    
    # Test case 1: array with distinct positive integers
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    assert solution.max(arr1) == 7
    
    # Test case 2: array with a mix of negative and positive integers
    arr2 = [-1, -100, 3, 99]
    assert solution.max(arr2) == 99
    
    # Test case 3: array with duplicate maximum values
    arr3 = [10, 20, 20, 5]
    assert solution.max(arr3) == 20
    
    # Test case 4: array with all elements the same
    arr4 = [5, 5, 5, 5]
    assert solution.max(arr4) == 5
    
    # Test case 5: array with only one element
    arr5 = [10]
    assert solution.max(arr5) == 10

def test_smax():
    solution = ArrayWarmup()
    
    # Test case 1: array with distinct positive integers
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    assert solution.smax(arr1) == 6
    
    # Test case 2: array with a mix of negative and positive integers
    arr2 = [-1, -100, 3, 99]
    assert solution.smax(arr2) == 3
    
    # Test case 3: array with duplicate maximum values
    arr3 = [10, 20, 20, 5]
    assert solution.smax(arr3) == 10
    
    # Test case 4: array with all elements the same
    arr4 = [5, 5, 5, 5]
    assert solution.smax(arr4) == 5  # Since there's no second distinct maximum, should return the same
    
    # Test case 5: array with only one element
    arr5 = [10]
    assert solution.smax(arr5) == 10  # With one element, smax should return the same as max


def test_is_sorted():
    solution = ArrayWarmup()
    
    # Test case 1: array is sorted in ascending order
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    assert solution.is_sorted(arr1) == True
    
    # Test case 2: array with mixed order (not sorted)
    arr2 = [3, 1, 4, 1, 5, 9, 2]
    assert solution.is_sorted(arr2) == False
    
    # Test case 3: array with all elements the same (sorted)
    arr3 = [5, 5, 5, 5, 5]
    assert solution.is_sorted(arr3) == True
    
    # Test case 4: array with only one element (sorted)
    arr4 = [10]
    assert solution.is_sorted(arr4) == True
    
    # Test case 5: empty array (considered sorted)
    arr5 = []
    assert solution.is_sorted(arr5) == True
    
    # Test case 6: array with negative numbers sorted in ascending order
    arr6 = [-100, -50, 0, 50, 100]
    assert solution.is_sorted(arr6) == True
    
    # Test case 7: array with duplicate elements (sorted)
    arr7 = [1, 2, 2, 3, 4]
    assert solution.is_sorted(arr7) == True


def test_remove_duplicates():
    solution = ArrayWarmup()
    
    # Test case 1: Normal case with multiple duplicates
    nums1 = [1, 1, 2, 2, 2, 3, 3]
    k1 = solution.remove_duplicates(nums1)
    assert k1 == 3  # Number of unique elements
    assert nums1[:k1] == [1, 2, 3]  # The first k elements should be [1, 2, 3]
    
    # Test case 2: Array with no duplicates
    nums2 = [1, 2, 3, 4, 5]
    k2 = solution.remove_duplicates(nums2)
    assert k2 == 5  # No duplicates, so length remains the same
    assert nums2[:k2] == [1, 2, 3, 4, 5]  # The array should remain the same
    
    # Test case 3: Array with all elements the same
    nums3 = [1, 1, 1, 1, 1]
    k3 = solution.remove_duplicates(nums3)
    assert k3 == 1  # Only one unique element
    assert nums3[:k3] == [1]  # The first element should be [1]
    
    # Test case 4: Array with two unique elements
    nums4 = [1, 1, 2]
    k4 = solution.remove_duplicates(nums4)
    assert k4 == 2  # Two unique elements
    assert nums4[:k4] == [1, 2]  # The first two elements should be [1, 2]
    
    # Test case 5: Array with one element
    nums6 = [1]
    k6 = solution.remove_duplicates(nums6)
    assert k6 == 1  # Only one element, so the length remains 1
    assert nums6[:k6] == [1]  # The array should remain the same


def test_rotate_left_one():
    solution = ArrayWarmup()
    
    # Test case 1: Rotating a normal array
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    rotated_nums1 = solution.rotate_left_one(nums1)
    assert rotated_nums1 == [2, 3, 4, 5, 1], f"Expected [2, 3, 4, 5, 1] but got {rotated_nums1}"
    
    # Test case 2: Rotating an array with repeated elements
    nums2 = [7, 7, 7, 7]
    rotated_nums2 = solution.rotate_left_one(nums2)
    assert rotated_nums2 == [7, 7, 7, 7], f"Expected [7, 7, 7, 7] but got {rotated_nums2}"
    
    # Test case 3: Rotating an array with two elements
    nums3 = [9, 1]
    rotated_nums3 = solution.rotate_left_one(nums3)
    assert rotated_nums3 == [1, 9], f"Expected [1, 9] but got {rotated_nums3}"
    
    # Test case 4: Rotating a single element array (no change expected)
    nums4 = [5]
    rotated_nums4 = solution.rotate_left_one(nums4)
    assert rotated_nums4 == [5], f"Expected [5] but got {rotated_nums4}"


def test_rotate1():
    solution = ArrayWarmup()  # Assuming the rotate function is in a class named Solution
    
    # Test case 1: Normal rotation
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    solution.rotate1(nums1, 3)
    assert nums1 == [4, 5, 6, 7, 1, 2, 3], f"Expected [4, 5, 6, 7, 1, 2, 3] but got {nums1}"
    
    # Test case 2: Rotating by length of array (no change expected)
    nums2 = [-1, -100, 3, 99]
    solution.rotate1(nums2, 4)
    assert nums2 == [-1, -100, 3, 99], f"Expected [-1, -100, 3, 99] but got {nums2}"
    
    # Test case 3: Rotating by more than length (k > len(nums))
    nums3 = [1, 2, 3]
    solution.rotate1(nums3, 5)  # 5 % 3 = 2
    assert nums3 == [3, 1, 2], f"Expected [3, 1, 2] but got {nums3}"
    
    # Test case 4: Rotating by 0 (no change expected)
    nums4 = [1, 2, 3, 4]
    solution.rotate1(nums4, 0)
    assert nums4 == [1, 2, 3, 4], f"Expected [1, 2, 3, 4] but got {nums4}"

    # Test case 5: Array with one element (no change expected)
    nums5 = [42]
    solution.rotate1(nums5, 1)
    assert nums5 == [42], f"Expected [42] but got {nums5}"


def test_rotate2():
    solution = ArrayWarmup()  # Assuming the rotate function is in a class named Solution
    
    # Test case 1: Normal rotation
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    solution.rotate2(nums1, 3)
    assert nums1 == [4, 5, 6, 7, 1, 2, 3], f"Expected [4, 5, 6, 7, 1, 2, 3] but got {nums1}"
    
    # Test case 2: Rotating by length of array (no change expected)
    nums2 = [-1, -100, 3, 99]
    solution.rotate2(nums2, 4)
    assert nums2 == [-1, -100, 3, 99], f"Expected [-1, -100, 3, 99] but got {nums2}"
    
    # Test case 3: Rotating by more than length (k > len(nums))
    nums3 = [1, 2, 3]
    solution.rotate2(nums3, 5)  # 5 % 3 = 2
    assert nums3 == [3, 1, 2], f"Expected [3, 1, 2] but got {nums3}"
    
    # Test case 4: Rotating by 0 (no change expected)
    nums4 = [1, 2, 3, 4]
    solution.rotate2(nums4, 0)
    assert nums4 == [1, 2, 3, 4], f"Expected [1, 2, 3, 4] but got {nums4}"

    # Test case 5: Array with one element (no change expected)
    nums5 = [42]
    solution.rotate2(nums5, 1)
    assert nums5 == [42], f"Expected [42] but got {nums5}"


def test_reverse_inplace():
    solution = ArrayWarmup()  # Assuming the reverse_inplace function is in a class named Solution
    
    # Test case 1: Normal list with multiple elements
    nums1 = [1, 2, 3, 4, 5]
    solution.reverse_inplace(nums1)
    assert nums1 == [5, 4, 3, 2, 1], f"Expected [5, 4, 3, 2, 1] but got {nums1}"
    
    # Test case 2: List with two elements
    nums2 = [1, 2]
    solution.reverse_inplace(nums2)
    assert nums2 == [2, 1], f"Expected [2, 1] but got {nums2}"
    
    # Test case 3: List with one element (no change expected)
    nums3 = [42]
    solution.reverse_inplace(nums3)
    assert nums3 == [42], f"Expected [42] but got {nums3}"
    
    # Test case 4: Empty list (no change expected)
    nums4 = []
    solution.reverse_inplace(nums4)
    assert nums4 == [], f"Expected [] but got {nums4}"
    
    # Test case 5: List with duplicate elements
    nums5 = [1, 2, 2, 3, 3]
    solution.reverse_inplace(nums5)
    assert nums5 == [3, 3, 2, 2, 1], f"Expected [3, 3, 2, 2, 1] but got {nums5}"

