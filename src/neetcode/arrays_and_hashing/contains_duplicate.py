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
        numsDict: dict[int, bool] = {}
        for i, v in enumerate(nums):
            if v in numsDict:
                return True
            numsDict[v] = True
        return False
