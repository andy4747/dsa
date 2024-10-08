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
        sDict: dict[str, int] = {}
        tDict: dict[str, int] = {}

        for i in range(len(s)):
            sDict[s[i]] = sDict.get(s[i], 0) + 1
            tDict[t[i]] = tDict.get(t[i], 0) + 1
        
        for char, count in sDict.items():
            if tDict.get(char) != count:
                return False
        return True

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = []
        for item in strs:
            sub_result = [item]
            for next_item in strs:
                check = self.isAnagram(item, next_item)
                if check:
                    sub_result.append(next_item)
            result.append(sub_result)
        return result

