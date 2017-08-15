# coding=utf8
# https://leetcode.com/problems/missing-number/description/
# Easy

# O(n)
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (len(nums) + 1) * len(nums) / 2 - sum(nums)

