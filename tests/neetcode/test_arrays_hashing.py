from src.neetcode.arrays_and_hashing.contains_duplicate import Solution as ContainsDuplicateSolution

def test_contains_duplicate():
    solution = ContainsDuplicateSolution()
    
    assert solution.containsDuplicate([1, 2, 3, 1]) == True
    assert solution.containsDuplicate([1, 2, 3, 4]) == False
    assert solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True