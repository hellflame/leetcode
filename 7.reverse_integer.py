# coding=utf8
# https://leetcode.com/problems/reverse-integer/description/
# Easy

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 2147483647 or x <= -2147483648:
            return 0
        x = str(x)
        if x.startswith('-'):
            result = - int(''.join(list(x[-1:0:-1])))
        else:
            result = int(''.join(list(x[::-1])))

        # return 0 when the reversed integer overflows.
        return 0 if result >= 2147483647 or result <= -2147483648 else result

