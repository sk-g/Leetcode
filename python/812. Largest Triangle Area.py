812. Largest Triangle Area.py
"""
Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
"""
class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """

        def area(p, q, r):
            a = dist(p,q)
            b = dist(q,r)
            c = dist(p,r)
            s = (a + b + c)/2
            # Herons formula
            if a<b+c and b<a+c and c<a+b:
                return math.sqrt(s*(s-a)*(s-b)*(s-c))
            else:#points that cannot form a triangle
                return -sys.maxsize
        def dist(a,b):
            return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

        return max(area(*triangle)
            for triangle in itertools.combinations(points, 3))   