#857. Minimum Cost to Hire K Workers
class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        workers = []
        for i in range(len(quality)):
            workers.append([wage[i]/quality[i],quality[i]])
        workers.sort(key = lambda x:x[0])
        #print(workers)
        heap = []
        res = float('inf')
        cum_sum = 0 
        for ratio,quality in workers:
            heapq.heappush(heap,-quality)
            cum_sum += quality
            if len(heap) > K:
                cum_sum += heapq.heappop(heap)
            if len(heap) == K:
                res = min(res, cum_sum * ratio)
        return res
        