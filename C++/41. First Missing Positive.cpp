class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        for(int i=0;i<n;++i)  
        {
            if(nums[i] <= 0)
            {
                nums[i] = (n+1);
            }
        }
        
        for(auto& num:nums)
        {
            if(abs(num)<=n && abs(num)>0)
                nums[abs(num)-1]>0? nums[abs(num)-1]*= -1 : nums[abs(num)-1];

        }
        
        for(int i=0;i<n;++i)
        {
            if(nums[i]>0)
                return i+1;
        }
        return n+1;
    }
};