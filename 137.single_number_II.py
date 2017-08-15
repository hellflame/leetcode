# coding=utf8
# https://leetcode.com/problems/single-number-ii/description/
# Medium

# O(n)

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (sum(set(nums)) * 3 - sum(nums)) / 2


