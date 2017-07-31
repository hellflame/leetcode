# coding=utf8
# https://leetcode.com/problems/happy-number/#/discuss
# Easy

def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """
    while n > 6:
        sum = 0
        while n:
            sum += (n % 10) ** 2
            n /= 10
        n = sum
    return n == 1

