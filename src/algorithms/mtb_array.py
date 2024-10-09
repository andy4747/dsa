class MTBArray:
    """
    MTB stands for master the basics. This is a class for performing basic operations on arrays (lists) in Python.

    This class provides methods to manipulate lists, including inserting elements 
    at the end. It is designed to help users master fundamental array operations 
    and understand how lists work in Python.

    Notes:
        - This class serves as a reference note for basic array manipulations.
    """
    def insert_at_last(self, nums:list[int], value:int) -> None:
        """
        Inserts the value at the end of the provided list.

        Args:
            nums (list[int]): The list to modify.
            value (int): The value to insert at the end of the list.

        Returns:
            None
        """
        n = len(nums)
        new_arr = [0] * (n+1)
        for i in range(n):
            new_arr[i] = nums[i]
        new_arr[n] = value
        nums.clear()
        nums.extend(new_arr)

    def insert_at_first(self, nums: list[int], value: int) -> None:
        """
        Inserts the value at the beginning of the provided list.

        Args:
            nums (list[int]): The list to modify.
            value (int): The value to insert at the beginning.

        Returns:
            None
        """
        n = len(nums)
        new_arr: list[int] = [0] * (n+1)
        new_arr[0] = value
        for i in range(n):
            new_arr[i+1] = nums[i]
        nums.clear()
        nums.extend(new_arr)
