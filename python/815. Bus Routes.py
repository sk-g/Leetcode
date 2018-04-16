#815. Bus Routes.py
"""
We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

Example:
Input: 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation: 
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Note:

1 <= routes.length <= 500.
1 <= routes[i].length <= 500.
0 <= routes[i][j] < 10 ^ 6.
"""
import collections, itertools
class Solution:
    def numBusesToDestination(self, routes, S, T):
        if S==T: return 0
        # construct a graph of bus lines instead of stations
        tmp = collections.defaultdict(set)
        for line, stations in enumerate(routes):
            for station in stations:
                tmp[station].add(line)
        graph = collections.defaultdict(set)
        for station, lines in tmp.items():
            for l1, l2 in itertools.combinations(lines,2):
                graph[l1].add(l2)
                graph[l2].add(l1)
        # BFS        
        dst = [l for l,st in enumerate(routes) if T in st] # end with bus lines to T
        explored = set()
        Q = collections.deque([l for l,st in enumerate(routes) if S in st]) # start from bus lines to S
        count = 1
        while Q: 
            for _ in range(len(Q)):
                node = Q.popleft()
                if node in dst: return count
                explored.add(node)
                for neighbour in graph[node]:
                    if neighbour not in explored:
                        Q.append(neighbour)
            count += 1
        return -1