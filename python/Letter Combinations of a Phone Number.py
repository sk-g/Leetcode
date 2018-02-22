# 17. Letter Combinations of a Phone Number

"""
Useless qeustion.
Easy trick with map.


"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if ''== digits: return []
        mp={'1':'*','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz','0':' '} # map numbers and letters
        'digits=digits.split()' # get a split of input
        return reduce(lambda acc, digit: [x + y for x in acc for y in mp[digit]], digits, ['']) # reduce + lambda + map <- popular for this
        																						# this kind of problems