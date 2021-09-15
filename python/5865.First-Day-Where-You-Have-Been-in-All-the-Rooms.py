from typing import *
import collections
class Solution:
    def firstDayBeenInAllRooms(self, A: List[int]) -> int:
        n = len(A)
        MOD = (10 ** 9) + 7
        if len(set(A)) == 1:
            return (2 ** n - 2) % MOD
        
        seen = collections.defaultdict(int)
        seen[0] = 1
        day = 0
        current_visit = 0
        while True:
            if seen[current_visit] %2 != 0: 
                # visited the current room odd times
                current_visit = A[current_visit]
            else:
                current_visit = (current_visit  +  1) % n
            # print(current_visit)
            seen[current_visit] +=  1
            day += 1
            print(day, current_visit)
            if len(seen) == n:
                return day % MOD
sol = Solution()
A = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(sol.firstDayBeenInAllRooms(A))
A = [0,0,1,2,4,0,1,6,0,0,2,3,4,3,4,11,6,0,16,14,20,16,9,9,1,8,8,4,14,13,5,12,8,18,27,34,36,13,10,35,13,31,13,29,2,45,17,30,10,18,41,14,41,22,2,4,1,15,27,35,12,10,46,25,61,8,65,57,48,61,8,35,2,66,47,5,54,76,73,51,13,64,15,2]
print(sol.firstDayBeenInAllRooms(A))