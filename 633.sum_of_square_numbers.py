# coding=utf8
# https://leetcode.com/problems/sum-of-square-numbers/description/
# Easy

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = int(c ** .5)
        while i >= 0:
            tmp = (c - i * i)
            sqt = int(tmp ** .5)
            if sqt * sqt == tmp:
                return True
            i -= 1
        return False

