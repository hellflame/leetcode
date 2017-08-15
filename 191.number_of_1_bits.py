# coding=utf8
# https://leetcode.com/problems/number-of-1-bits/description/
# Easy

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')
        
