// 683
// sanjay
// google snapshot challenge question 2
// located in coding questions/Google/

/*
There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.

Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.

If there isn’t such day, output -1.

solution source: http://zxi.mytechroad.com/blog/simulation/leetcode-683-k-empty-slots/
*/
// Author: Huahua
// Runtime: 196 ms (better than 94%)
class Solution {
public:
    int kEmptySlots(vector<int>& flowers, int k) {
        int n = flowers.size();
        if (n == 0 || k >= n) return -1;
        ++k;
        int bs = (n + k - 1) / k;
        vector<int> lows(bs, INT_MAX);
        vector<int> highs(bs, INT_MIN);
        for (int i = 0; i < n; ++i) {
            int x = flowers[i];
            int p = x / k;
            if (x < lows[p]) {
                lows[p] = x;
                if (p > 0 && highs[p - 1] == x - k) return i + 1;
            } 
            if (x > highs[p]) {
                highs[p] = x;
                if (p < bs - 1 && lows[p + 1] == x + k) return i + 1;
            }            
        }
        
        return -1;
    }
};

// brute force

// Author: Huahua
// Runtime: 192 ms (better than 97.85%)
class Solution {
public:
    int kEmptySlots(vector<int>& flowers, int k) {
        int n = flowers.size();
        if (n == 0 || k >= n) return -1;
        std::unique_ptr<char[]> f(new char[n+1]);
        memset(f.get(), 0, (n + 1)*sizeof(char));
        for (int i = 0; i < n; ++i)
            if (IsValid(flowers[i], k, n, f.get()))
                return i + 1;
        return -1;
    }
private:
    bool IsValid(int x, int k, int n, char* f) {
        f[x] = 1;
        if (x + k + 1 <= n && f[x + k + 1]) {
            bool valid = true; 
            for (int i = 1; i <= k; ++i)
                if (f[x + i]) {
                    valid = false;
                    break;
                }
            if (valid) return true;
        }
        if (x - k - 1 > 0 && f[x - k - 1]) {            
            for (int i = 1; i <= k; ++i)
                if (f[x - i]) return false;
            return true;
        }
        return false;
    }
};

// BST

/ Author: Huahua
// Runtime: 228 ms
class Solution {
public:
    int kEmptySlots(vector<int>& flowers, int k) {
        int n = flowers.size();
        if (n == 0 || k >= n) return -1;        
        set<int> xs;        
        for (int i = 0; i < n; ++i) {
            int x = flowers[i];
            auto r = xs.insert(x).first;
            auto l = r;
            if (++r != xs.end() && *r == x + k + 1) return i + 1;
            if (l != xs.begin() && *(--l) == x - k - 1) return i + 1;
        }
        
        return -1;
    }
};