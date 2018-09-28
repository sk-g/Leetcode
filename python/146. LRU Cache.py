class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.d = dict()
        self.q = collections.deque([],maxlen = capacity)
        self.c = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.d:
            return -1
        else:
            self.q.remove(key)
            self.q.appendleft(key)
            return self.d[key]
        

    def put(self, key, value):
        if key in self.d:
            self.q.remove(key)
        elif len(self.d) == self.c:
            popped = self.q.pop()
            self.d.pop(popped)
        self.d[key] = value
        self.q.appendleft(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)