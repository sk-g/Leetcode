# 388. Longest Absolute File Path
# medium
# describption: https://leetcode.com/problems/longest-absolute-file-path/description/
# if you cannot open : https://imgur.com/a/TUE4h

class Solution:
    def lengthLongestPath(self, x):
        """
        :type input: str
        :rtype: int
        The number of tabs is my depth and for each depth I store the current path length.
        """
        h = {0:0}
        maxlen = 0
        #print(x.splitlines())
        for line in x.splitlines():
            name = line.lstrip('\t')
            depth = len(line)-len(name)
            if name.count('.') != 0:
                maxlen = max(maxlen,h[depth]+len(name))
            else:
                h[depth +1] = h[depth] + len(name) + 1
        return maxlen

# another approach

class Solution:
    def count_tab(self, s):
        ret = 0
        for c in s:
            if c == '\t':
                ret += 1
            else:
                break
        return ret, s[ret:]
    
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        path = []
        maxlen = 0
        for name in input.split('\n'):
            level, name = self.count_tab(name)
            path = path[:level] + [name]
            if '.' in path[-1]:
                maxlen = max(maxlen, len('/'.join(path)))
        return maxlen        

# most common solution

class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        input += '\n'
        
        levels = {0:0}
        level = 1

        path_counter = 0
        
        max_length = 0
        
        file = False
        
        for i, c in enumerate(input):
            if c == '\n':
                if file:
                    path_length = path_counter + levels[level - 1] + level - 1
                    if path_length > max_length:
                        max_length = path_length
                
                print(level, path_counter)
                levels[level] = levels[level - 1] + path_counter
                
                level = 1
                path_counter = 0
                file = False
            elif c == '\t':
                level += 1
            else:
                if c == '.':
                    file = True
                path_counter += 1
        
        return max_length        