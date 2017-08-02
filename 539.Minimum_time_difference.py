# coding=utf8
# https://leetcode.com/problems/minimum-time-difference/description/
# Medium


# O(nlog n)

class Solution(object):
    def to_num(self, point):
        s = point.split(":")
        result = int(s[0]) * 60 + int(s[1])
        return result
    
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        index = 1
        m = 1440
        target = [self.to_num(x) for x in timePoints]
        target.sort() # O(nlogn)
        while index < len(target):
            diff = target[index] - target[index - 1]
            if diff > 720 and 1440 - diff < m:
                m = 1440 - diff
            elif diff < m:
                m = diff
            index += 1
        if 1440 - target[-1] + target[0] < m:
            return 1440 - target[-1] + target[0]
        return m
  
      
# O(n2)
class Solution(object):
    def to_num(self, point):
        s = point.split(":")
        result = int(s[0]) * 60 + int(s[1])
        return result
    
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        index_x = 0
        m = 1440
        target = [self.to_num(x) for x in timePoints]
        while index_x < len(target):
            index_y = index_x + 1
            while index_y < len(target):
                dif = abs(target[index_x] - target[index_y])
                if not dif:
                    return 0
                else:
                    if dif > 720 and (1440 - dif) < m:
                        m = 1440 - dif
                    elif dif < m:
                        m = dif
                index_y += 1
            index_x += 1
        return m
        