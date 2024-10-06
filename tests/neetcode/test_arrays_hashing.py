from src.neetcode.arrays_and_hashing.contains_duplicate import Solution as ContainsDuplicateSolution
from src.neetcode.arrays_and_hashing.valid_anagram import Solution as ValidAnagram

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

