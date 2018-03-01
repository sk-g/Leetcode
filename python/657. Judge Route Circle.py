#657. Judge Route Circle
"""
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false


neat solution form submission details: # same run time,concept
return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
"""

# count and check each

from collections import Counter
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        counts = Counter(moves)
        k,v = list(counts.keys()),list(counts.values())
        
        if 'L' in k and 'R' in k and 'U' in k and 'D' in k:
            return(counts['L']==counts['R'] and counts['D'] == counts['U'])
        elif 'L' in k and 'R' in k and 'U' not in k and 'D' in k:
            return False
        elif 'L' in k and 'R' in k and 'U' not in k and 'D' not in k:
            return(counts['L'] == counts['R'])
        elif 'L' not in k and 'R' not in k and 'U' in k and 'D' in k:
            return(counts['U'] == counts['D'])
        else:
            return False