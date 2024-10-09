class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Returns true if the the number is palindrome, otherwise returns False.

        Args:
            x: the number to check if it is palindrome or not.

        Returns:
            bool: The boolean value by checking if x is palindrome or not.
        """
        if x < 0:
            return False
        reversed = 0
        temp = x
        while temp != 0:
            last_digit = temp % 10
            reversed = reversed * 10 + last_digit
            temp //= 10
        return reversed == x
