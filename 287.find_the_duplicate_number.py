# coding=utf8
# https://leetcode.com/problems/find-the-duplicate-number/description/
# Medium

# O(n)

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (sum(nums) - sum(set(nums))) / (len(nums) - len(set(nums)))


