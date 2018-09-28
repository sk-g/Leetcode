class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = [int(i) for i in version1.split(".")]
        v2 = [int(i) for i in version2.split(".")]
        
        for i in range(max(len(v1),len(v2))):
            v1_ = v1[i] if i < len(v1) else 0
            v2_ = v2[i] if i < len(v2) else 0
            
            if v1_ > v2_:
                return 1
            elif v1_ < v2_:
                return -1
        return 0