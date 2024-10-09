class Solution:
    def removeElement(self, nums: list[int|str], val: int) -> int:
        """
        removes all the occurance of val:int from the nums:list[list] array, and returns the new length

        Args:
            nums: The array to remove duplicates from.
            val: The value to which remove from the array.

        Returns:
            int: The new lenght of the array after removing elements.
        """
        index = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index
