# 771. Jewels and Stones
"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have. 
Each character in S is a type of stone you have.  
You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Simple dictionary based solution and a Set based solution both counting letters in common.

dictionary : 57 ms
set: 48 ms

Note : I used Counter because I am lazy to count values.
can write manual code to count items but it will be slow.

"""

from collections import Counter 
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        j_counter = Counter(J)
        s_counter = Counter(S)
        j_keys,s_keys,res = list(j_counter.keys()),list(s_counter.keys()),0
        for i in s_keys:
                if i in j_keys:
                    res += max(j_counter[i],s_counter[i])
        return res
        
        #### set based ####
        setJ = set(J)
        return sum(s in setJ for s in S)
        
        
