class ArrayWarmup:
    """
    Warmup questions of arrays from strivers A2Z Easy Array Questions
    """
    def max(self, arr: list[int]) -> int:
        """
        Returns the largest element in the array arr.

        Args:
            arr: The array to check for largest element.
        """
        max = arr[0]
        for item in arr:
            if item > max:
                max = item
        return max
    
    def smax(self, arr: list[int]) -> int:
        """
        Returns the second largest element in the array arr.

        Args:
            arr: The arrary to check for second largest element.
        """
        max = self.max(arr)
        _smax = arr[0]
        for item in arr:
            if item > _smax and item < max:
                _smax = item
        return _smax

    def is_sorted(self, arr: list[int]) -> bool:
        """
        Returns True if the array is sorted, otherwise false

        Args:
            arr: The array to check if it is sorted or not.
        """
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                return False
        return True

    def remove_duplicates(self, nums: list[int]) -> int:
        """
        Returns the new length of the non-descending order array after removing the duplicates.

        Args:
            nums: The non-descending order array to remove duplicates from.
        """
        hs = set()
        for item in nums:
            hs.add(item)
        new_len = len(hs)
        i = 0
        for item in hs:
            nums[i] = item
            i+=1
        return new_len

    def rotate_left_one(self, nums: list[int]) -> list[int]:
        """
        Returns the new array by shifting one position to the left.

        Args:
            nums: The array to left rotate by one position.
        """
        n = len(nums)
        temp = nums[0]
        for i in range(1, n):
            nums[i-1] = nums[i]
        nums[n-1] = temp
        return nums


    def rotate1(self, nums: list[int], k: int) -> None: 
        """
        Rotates the array by k positions to the left and returns nothing.
        
        Approach: shift one k item at a time in a loop and store 1st item then place it at end of the arr at end of each cycle.

        Args:
            nums: The array to rotate.
            k: The number of elements to shift to left.

        Time Complexity: O(n*d)
        Space Complexity: O(1)
        """
        n = len(nums)
        for i in range(k):
            first=nums[0]
            for j in range(n-1):
                nums[j] = nums[j+1]
            nums[n-1] = first


    def rotate2(self, nums: list[int], k: int) -> None:
        """
        Rotates the array by k positions to the left and returns nothing.

        Approach: create a temp array, store last n-k elements in first of temp arr, and copy first k elements to last of temp.

        Args:
            nums: The array to rotate.
            k: The number of elements to shift to left.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(nums)
        k %= n
        temp = [0]*n
        for i in range(n-k):
            temp[i]=nums[k+i]
        for i in range(k):
            temp[n-k+i]=nums[i]
        for i in range(n):
            nums[i] = temp[i]

    def reverse_inplace(self, nums: list[int]) -> None:
        """
        Reverse the array in place.

        Args:
            nums: The array to reverse
        """
        n=len(nums)
        left=0
        right=n-1
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1
