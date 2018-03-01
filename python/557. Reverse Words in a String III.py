"""
557. Reverse Words in a String III

"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split(' ')
        s=map(lambda x: x[::-1],s)
        s=' '.join(s)
        return s


"""
simpler, cleaner, faster

class Solution:
    def reverseWords(self, s):
        
        #:type s: str
        #:rtype: str
        
        temp = s.split(' ')
        for i in range(len(temp)):
            temp[i] = temp[i][::-1]
        return(' '.join([i for i in temp]))
"""        