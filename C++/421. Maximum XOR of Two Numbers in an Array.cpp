//421. Maximum XOR of Two Numbers in an Array

class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        int n = nums.size();
        
        if (n == 0 || n == 1)
            return 0;
        if (n == 2)
            return nums.at(0) ^ nums.at(1);
        int res = 0;
        for(int i = 0;i<nums.size()-1;++i){
            for(int j = i+1; j<nums.size();++j){
                int x = nums[i]^nums[j];
                res = ((res>x)?res:x);
            }
        }
        return res;
    }
};