# coding=utf8
# https://leetcode.com/problems/plus-one/description/
# Easy

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        inc = 0
        digits[i] += 1
        while i >= 0:
            tmp = digits[i] + inc
            digits[i] = tmp % 10
            inc = tmp / 10
            i -= 1
        if inc:
            return [inc] + digits
        return digits

