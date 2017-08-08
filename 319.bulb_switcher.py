# coding=utf8
# https://leetcode.com/problems/bulb-switcher/description/
# Medium

# solution 1
# O(1)
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(n ** .5)


# solution 2
# O(n)
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """

        start = 2 ** n - 1
        index = 1
        while index < n:
            start ^= int((("0" * index + '1') * (n / index + 1))[0:n], 2)
            index += 1
        
        return bin(start).count('1')