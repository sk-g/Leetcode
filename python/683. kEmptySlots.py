# 683
# sanjay
"""
There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.

Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.

If there isn’t such day, output -1.

solution source: http://zxi.mytechroad.com/blog/simulation/leetcode-683-k-empty-slots/

"""
def kEmptySlots(flowers, k):
    n = len(flowers)
    f = [0] * (n + 1)
    i = 0
    
    def isValid(x, k, n, f):
        f[x] = 1
        if x + k + 1 <= n and f[x + k + 1] == 1:
            valid = True
            for i in range(k):
                if f[x + i + 1] == 1: 
                    valid = False
                    break
            if valid: return True
        if x - k - 1 > 0 and f[x - k - 1] == 1:
            for i in range(k):
                if f[x - i - 1] == 1:
                    return False
            return True
        return False
    
    for x in flowers:
        i += 1
        if isValid(x, k, n, f): return i
    
    return -1
print(kEmptySlots([3,1,5,4,2],2))
print(kEmptySlots([3,1,5,4,2],1))