class Solution:
    """
    Leetcode 217: Contains Duplicate
    """
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Check if the array contains any duplicates.

        Args:
            nums: The array to check for duplicates.
        """
        result: dict[int, bool] = {}
        for v in nums:
            if v in result:
                return True
            result[v]=True
        return False
