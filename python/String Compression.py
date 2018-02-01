# 443. String Compression
class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        here = 0 # start replacing from here
        i = 0 # iterator
        while i < len(chars): #iterate through array
            char = chars[i] # current character 
            length = 1 # current characters length
            while i+1 < len(chars) and char == chars[i+1]: # the last char
                length += 1 # increase current chars length
                i += 1  # increment pointer/iterator
            chars[here] = char # replace the character at poisition with current char
            if length > 1: # only replace if current char is seen more than once
                len_str = str(length)
                chars[here+1:here + 1 + len(str(length))] = str(length) # here to there = length = repeat length of current char
                here += len(str(length)) # if length > 10, replace it as "1", "0" so "there" value changes
            here += 1 # if no repetitions, move on to the next char
            i += 1 # incrementing the iterator
        #print(chars[:here])
        return here