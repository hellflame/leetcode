# coding=utf8
# https://leetcode.com/problems/power-of-two/description/
# Easy


import re
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 时快时慢的=。=，有时超过75%，有时超过 0.4% 
        return bool(re.match("0b10{0,}$", bin(n)))
        
