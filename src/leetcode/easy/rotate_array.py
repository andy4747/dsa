class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Rotate an array to the right by k steps.
        
        Args:
            nums: A list of integers to be rotated.
            k: The number of steps to rotate the array.
        
        Example:
            >>> nums = [1, 2, 3, 4, 5, 6, 7]
            >>> k = 3
            >>> Solution().rotate(nums, k)
            >>> nums
            [5, 6, 7, 1, 2, 3, 4]
        
        Time Complexity:
            O(n) where n is the length of nums
        
        Space Complexity:
            O(1) as we modify the array in-place
        """
        def reverse(nums: list[int], start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        n = len(nums)
        k = k % n  # Handle cases where k > n
        
        # Reverse the entire array
        reverse(nums, 0, n - 1)
        # Reverse the first k elements
        reverse(nums, 0, k - 1)
        # Reverse the remaining elements
        reverse(nums, k, n - 1)
