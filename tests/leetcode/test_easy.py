from src.leetcode.easy.rotate_array import Solution as RotateArraySolution

def test_rotate_array():
    solution = RotateArraySolution()
    
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    solution.rotate(nums1, 3)
    assert nums1 == [5, 6, 7, 1, 2, 3, 4]
    
    nums2 = [-1, -100, 3, 99]
    solution.rotate(nums2, 2)
    assert nums2 == [3, 99, -1, -100]