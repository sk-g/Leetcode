# 229
# Majority Element II
# can be solved in one pass. Well two: Boyer-Moore Majority Vote algorithm
# or use dictionary to track frequency of all elements in array

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a={}
        for i in nums:
            if a.get(i,-1)==-1:
                a[i]=1
            else:
                a[i]+=1
        print a
        b=[]
        for i in a.keys():
            if a[i]>(len(nums)/3):
                b.append(i)
        
        return b
"""
# Boyer-Moore Majority Vote algorithm
# two contenders because n/3 => there could be (atmost) two majority elements.
# why "atmost"> 2*(n/3) => two elements appeared at least n/3 times and remaining 1/3
# cannot be majority.
def majorityElement(self, nums):
    if not nums:
        return []
    count1, count2, candidate1, candidate2 = 0, 0, 0, 1
    for n in nums:
        if n == candidate1:
            count1 += 1
        elif n == candidate2:v
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = n, 1
        elif count2 == 0:
            candidate2, count2 = n, 1
        else:
            count1, count2 = count1 - 1, count2 - 1
    return [n for n in (candidate1, candidate2)
                    if nums.count(n) > len(nums) // 3]
"""