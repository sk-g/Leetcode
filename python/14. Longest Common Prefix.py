#14. Longest Common Prefix

"""
Write a function to find the longest common prefix string amongst an array of strings.

"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        minLen = len(strs[0])
        for sx in strs:
            minLen = min(minLen,len(sx))
        res = ""
        for i in range(minLen):
            c = strs[0][i]
            for sx in strs:
                if sx[i] != c:
                    return res
            res += c
        return res