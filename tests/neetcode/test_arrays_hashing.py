from src.neetcode.arrays_and_hashing.contains_duplicate import Solution as ContainsDuplicateSolution
from src.neetcode.arrays_and_hashing.valid_anagram import Solution as ValidAnagram
from src.neetcode.arrays_and_hashing.two_sums import Solution as TwoSums

def test_contains_duplicate():
    solution = ContainsDuplicateSolution()
    
    assert solution.containsDuplicate([1, 2, 3, 1]) == True
    assert solution.containsDuplicate([1, 2, 3, 4]) == False
    assert solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True

def test_valid_anagram():
    solution = ValidAnagram()

    # Test cases with valid anagrams
    assert solution.isAnagram("anagram", "nagaram") == True, "Test case 1 failed"
    assert solution.isAnagram("listen", "silent") == True, "Test case 2 failed"
    
    # Test cases with invalid anagrams
    assert solution.isAnagram("rat", "car") == False, "Test case 3 failed"
    assert solution.isAnagram("hello", "bello") == False, "Test case 4 failed"
    
    # Edge cases with empty strings
    assert solution.isAnagram("", "") == True, "Test case 5 failed"
    
    # Test case with one empty string and one non-empty string
    assert solution.isAnagram("a", "") == False, "Test case 6 failed"
    
    # Test cases with different lengths
    assert solution.isAnagram("abcd", "abc") == False, "Test case 7 failed"
    
    # Case-sensitive check (should be False because anagram is case-sensitive)
    assert solution.isAnagram("Anagram", "nagaram") == False, "Test case 8 failed"
    
    # Test case with single characters
    assert solution.isAnagram("a", "a") == True, "Test case 9 failed"
    assert solution.isAnagram("a", "b") == False, "Test case 10 failed"


def test_twoSum():
    solution = TwoSums()  # Assuming the twoSum function is in a class named Solution
    
    # Test case 1: Normal list with a valid pair
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    assert result1 == [0, 1] or result1 == [1, 0], f"Expected [0, 1] or [1, 0] but got {result1}"
    
    # Test case 2: Pair at the beginning of the list
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    assert result2 == [1, 2] or result2 == [2, 1], f"Expected [1, 2] or [2, 1] but got {result2}"
    
    # Test case 3: Pair at the end of the list
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    assert result3 == [0, 1] or result3 == [1, 0], f"Expected [0, 1] or [1, 0] but got {result3}"
    
    # Test case 4: List with negative numbers
    nums4 = [-3, 4, 3, 90]
    target4 = 0
    result4 = solution.twoSum(nums4, target4)
    assert result4 == [0, 2] or result4 == [2, 0], f"Expected [0, 2] or [2, 0] but got {result4}"
    
    # Test case 5: No valid pair (should handle gracefully, may return an empty list or raise an exception)
    nums5 = [1, 2, 3]
    target5 = 7
    try:
        result5 = solution.twoSum(nums5, target5)
        assert not result5, f"Expected no valid pair but got {result5}"
    except ValueError as e:
        print("Handled gracefully with ValueError:", str(e))
    
    # Test case 6: Pair where both numbers are the same
    nums6 = [5, 5, 5]
    target6 = 10
    result6 = solution.twoSum(nums6, target6)
    assert result6 == [0, 1] or result6 == [1, 0], f"Expected [0, 1] or [1, 0] but got {result6}"

