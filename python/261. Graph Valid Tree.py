class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n-1:
            return False
        graph = collections.defaultdict(list)
        for x,y in edges:
            graph[x] += y,
            graph[y] += x,
        
        q = collections.deque([0])
        visited = set()
        while q:
            node = q.pop()
            if node in visited:
                return False
            visited.add(node)
            for nbr in graph[node]:
                q.append(nbr)
                graph[nbr].pop(graph[nbr].index(node))
                
        return all([i in visited for i in range(n)])