# 169 Majority Element
# Easiest of an interesting type of problem
# pythonic way to return middle number of sorted array
# logic: if a number appears [n/2] or more times then it must fall in middle too
# after sorting
# other interesting approaches: Boyer - Moore Majority Algorithm
# Difficulty: Easy
# Commpanies: Adobe
# Topics: Sorting ( Divide and Conquer)
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]

        """
        # another easy to understand, simple solution:
        # Boyer - Moore Majority Algorithm
        # advantage: no sorting required, constant space
        counter = 0 
        current = 0
        for i in nums:
        	if counter == 0:
        		current,counter = i,1
        	elif i == current:
        		counter += 1
        	else:
        		counter -= 1
        return current

        """
        