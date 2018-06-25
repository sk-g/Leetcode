136. Single Number
static int __ = []() {
    std::ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return 0;
}();
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        /*
        int res = 0;
        for(int i = 0; i<nums.size();++i){
            res = res ^ nums[i];
        }
        return res;
        */
        int result = 0;
        for(auto num : nums)
        {
            result ^= num;
        }       
        return result;        
    }
};