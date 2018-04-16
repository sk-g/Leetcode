#68. Text Justification.py

"""
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:

[
   "This    is    an",
   "example  of text",
   "justification.  "
]
 

Note: Each word is guaranteed not to exceed L in length.

# more corner cases that piss you off than you can actually learn something
"""
class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res,cur,letters = [],[],0
        for w in words:
            if len(w) + len(cur) + letters > maxWidth:
                if len(cur) == 1:
                    res.append(cur[0]+' '*(maxWidth-letters))
                else:
                    spaces = maxWidth-letters
                    # distributed spaces equally with words
                    space_between_words, num_extra_spaces = divmod( spaces, len(cur)-1)
                    for i in range(num_extra_spaces):
                        cur[i] += ' '
                    res.append( (' '*space_between_words).join(cur) )
                cur, letters = [], 0                        
            cur += [w]
            letters += len(w)
        res.append(' '.join(cur) + ' '*(maxWidth - letters - len(cur) + 1) )
        return res