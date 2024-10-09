class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        returns the majority element in the array, which is, if an element occurs more than n/2 times, where n is the length of the array.

        Args:
            nums: The list to find the majority element on.

        Returns:
            int: returns the value that occurs more than n/2 times

        Summary:
            - The ...
            - ...
            - ...
        """
        n = len(nums)
        nMap = {}
        for v in nums:
            nMap[v] = nMap.get(v, 0) + 1
        
        n = n // 2
        for element, count in nMap.items():
            if count > n:
                return element
        return  -1
