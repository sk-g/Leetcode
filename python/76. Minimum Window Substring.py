#76. Minimum Window Substring.py
"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"

Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""
rom collections import Counter as counter
import sys
class Solution:
    
    def minWindow(self, s, t):

        d = {}
        l = 0
        st, en = 0, len(s)-1 # start, end
        f = 0
        for i in t:
            if i in d:
                d[i] += 1#counts
            else:
                d[i] = 1
                l += 1 #count unique
        for i in range(len(s)): # iterate
            if s[i] not in d:
                continue # move
            d[s[i]] -= 1 # decrease count if found
            if d[s[i]] == 0: # counts tallied
                l -= 1 # check remaining
            if l == 0: 
                start = f
                while True:
                    #print(d,i,start,s[start],st,en)
                    if s[start] in d:
                        if d[s[start]] < 0:
                            d[s[start]] += 1
                            start += 1
                            continue
                        else:
                            break
                    else:
                        start += 1
                        continue
                f = start
                if i - start < en - st:
                    st, en = start, i                    
        return s[st:en+1] if l == 0 else ''