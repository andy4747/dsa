
class Solution:
    """
    A class to solve the Two Sum problem.

    The Two Sum problem is defined as follows:
        Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

    Assumptions:
        - Each input would have exactly one solution.
        - The same element cannot be used twice.
        - The return format is a list of two integers representing the indices.
    """

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Approach: Hashmap

        Finds two indices in `nums` such that the numbers at those indices add up to `target`.
        
        Args:
            nums (List[int]): A list of integers.
            target (int): The target sum for which two numbers are to be found.

        Returns:
            List[int]: A list of two indices whose values add up to the target.

        Example:
            >>> solution = Solution()
            >>> solution.twoSum([2, 7, 11, 15], 9)
            [0, 1]
        
        In this example, nums[0] + nums[1] = 2 + 7 = 9, which is equal to the target.
        """
        numsDict: dict[int, int] = {}
        for i, v in enumerate(nums):
            more = target - v
            if more in numsDict:
                return [numsDict[more], i]
            numsDict[v] = i
        return []

    def twoSumBF(self, nums: list[int], target: int) -> list[int]:
        """
        Finds two indices in `nums` such that the numbers at those indices add up to `target`.

        Approach: Bruteforce
        
        Args:
            nums (List[int]): A list of integers.
            target (int): The target sum for which two numbers are to be found.



        Returns:
            List[int]: A list of two indices whose values add up to the target.

        Example:
            >>> solution = Solution()
            >>> solution.twoSum([2, 7, 11, 15], 9)
            [0, 1]
        
        In this example, nums[0] + nums[1] = 2 + 7 = 9, which is equal to the target.
        """
        result = []
        n=len(nums)
        for i, v in enumerate(nums):
            for j, w in enumerate(nums):
                if i != j:
                    sum = v + w
                    if sum == target:
                        result.append(i)
                        result.append(j)
                        return result
        return result
