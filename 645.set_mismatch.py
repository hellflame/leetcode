# coding=utf8
# https://leetcode.com/problems/set-mismatch/description/
# Easy

# O(n)
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        full = n * (1 + n) / 2
        less = sum(set(nums))
        more = sum(nums)
        return [more - less, full - less]

