# coding=utf8
# https://leetcode.com/problems/valid-perfect-square/description/
# Easy

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # this is actually cheat
        return int(num ** .5) ** 2 == num

