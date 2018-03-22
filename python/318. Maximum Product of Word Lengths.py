318. Maximum Product of Word Lengths
"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.

Medium
Google

Solution: mask based bit manipulation technique. Change strings into corresponding masks, use and, and then dp
"""

class Solution:
    def maxProduct(self, words):
        """
        # first solution is correct but TLE
        d = {}
        ans = 0
        words2 = [len(i) for i in words] #stpring lengths for later, so space overhead too
        words = [list(set(i)) for i in words]
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j:
                    for t in range(len(words[i])):
                        flag = False
                        if words[i][t] in words[j]:
                            flag = True
                            break

                    if not flag:    
                        ans = max(ans,words2[i]*words2[j])
                        #ans = max(ans, (len(words2[i]))*(len(words2[j])))
        
        return(ans)
        """
        if not words:
            return 0

    
        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask |= (1 << (ord(c) - 97))
            d[mask] = max(d.get(mask, 0), len(w))
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])    