# coding=utf8
# https://leetcode.com/problems/single-number/description/
# Easy

# O(n)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(set(nums)) * 2 - sum(nums)

