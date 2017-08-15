# coding=utf8
# https://leetcode.com/problems/climbing-stairs/description/
# Easy


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 斐波那契
        a = b = 1
        for _ in xrange(n):
            a, b = b, a + b
        return a
