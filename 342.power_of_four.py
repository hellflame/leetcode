# coding=utf8
# https://leetcode.com/problems/power-of-four/description/
# Easy

import re

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 时快时慢=。=
        return bool(re.match("0b1(00){0,}$", bin(num)))
        
