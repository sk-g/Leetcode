/*
        674. Longest Continuous Increasing Subsequence

        if len(nums) < 1:
            return 0
        cur_len = 1
        max_len = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                cur_len = cur_len + 1
            else:
                cur_len = 1
                
            if cur_len > max_len:
                max_len = cur_len
        return max_len

*/
static int x = []() { std::ios::sync_with_stdio(false); cin.tie(NULL); return 0; }();

class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        if(nums.size()<1){
            return 0;
        }
        int current = 1;
        int max = 1;
        for(int i=1;i<nums.size();++i){
            current = (nums[i]>nums[i-1])?current+1:1;
            max = (current>max)?current:max;
        }
        return max;
    }
};