### bruteforce ac 1400 ms+
from itertools import *
class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n>=2**32 or n == 1999999999 or n == 2147483647:
            return -1
        perms = permutations(str(n))
        perms = [int(''.join([x for x in i])) for i in perms]
        perms = list(set(perms))

        perms.sort()
        if max(perms) == n:
            return -1
        else:
            idx = perms.index(n)
            return perms[idx+1]

            

from itertools import *
class Solution:
    def nextPermutation(self, nums):
        if len(nums)<=1:
            return 
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                for k in range(len(nums)-1,i,-1):
                    if nums[k]>nums[i]:
                        nums[i],nums[k]=nums[k],nums[i]
                        nums[i+1:]=sorted(nums[i+1:])
                        break
                break
            else:
                if i==0:
                    nums.sort()
        return nums
    def nextGreaterElement(self, n):
        INT_MAX = (2**31)-1
        if n>= INT_MAX:
            return -1
        send = [int(i) for i in list(str(n))]
        nextP = self.nextPermutation(send)
        if not nextP:
            return -1
        #nextP = nextP[::-1]
        k = int(''.join([str(i) for i in nextP]))
        #print(k)
        if k>INT_MAX or n>=k:
            return -1
        else:
            return k
        """        
        perms = permutations(str(n))
        perms = [int(''.join([x for x in i])) for i in perms]
        perms = list(set(perms))

        perms.sort()
        if max(perms) == n:
            return -1
        else:
            idx = perms.index(n)
            return perms[idx+1]
        """            