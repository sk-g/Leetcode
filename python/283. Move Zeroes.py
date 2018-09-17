class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nz = nums.count(0)
        
        ci = 0
        
        for num in nums:
            if num != 0:
                nums[ci] = num
                ci += 1
        for i in range(len(nums)-nz,len(nums)):
            nums[i] = 0