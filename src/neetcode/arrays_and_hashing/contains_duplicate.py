class Solution:
    """
    Leetcode 217: Contains Duplicate
    """
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Check if the array contains any duplicates.

        Args:
        nums (List[int]): The array to check for duplicates.

        Returns:
        bool: True if the array contains duplicates, False otherwise.
        """
        return len(nums) != len(set(nums))
