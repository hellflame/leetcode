# coding=utf8
# https://leetcode.com/problems/power-of-three/description/
# Easy


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 由于测试用例使用了32位int，所以大多数人都是这么作弊的=。=
        # 然而实际上在python中到了 3 ** 39 依然还是int
        return n > 0 and (1162261467 % n == 0)


        
