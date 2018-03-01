class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # probably the most common question and the easiest to start with
        # I know of two solutions: 
            # First using dictionary (one pass and two pass)
            # The other using binary search (log(n))
        
        """ 
        One pass (O(n)) solution using dictionary

        if len(nums) <2: # handling some end cases quickly
            return
        if nums[0]+nums[1] == target:   return[0,1] # just checking if 
                                                    # we get lucky with first two numbers
        else:
            a = {} #empty dictionary
            for i in range(len(nums)):
                if nums[i] in a:    #if the current number found in dictionary
                    return([i,a[nums[i]]]) #return the poisition from list and dict
                else: # or 
                    a[target - nums[i]] = i # dictionary key with target - current value
                                            # and value as the poisition
                    
        """
        # same as above but without the fancy checks
        a = {}
        for i in range(len(nums)):
            if nums[i] in a:
                return([i,a[nums[i]]])
            else:
                a[target - nums[i]] = i
        """
        yet another way to use the same 
        logic
        # 44 ms beats 100% in python3
        seen = {}
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[target-nums[i]] = i
            else:
                #print("{} is in seen".format(nums[i]))
                return([seen[nums[i]],i])
        """
        