class Solution:
    """
    Leetcode 242: Valid Anagram
    """
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Returns true if t is anagram of s, and false otherwise.

        Args:
            s: The first input string
            t: Second input string

        """
        if len(s) != len(t):
            return False

        sDict:dict[str, int] = {}
        tDict:dict[str, int] = {}

        #add the char to map
        for i in range(len(s)):
            sDict[s[i]] = sDict.get(s[i], 0)+1
            tDict[t[i]] = tDict.get(t[i], 0)+1

        #compare the maps
        for char, count in sDict.items():
            if tDict.get(char, 0) != count:
                return False
        return True
