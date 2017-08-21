# coding=utf8
# https://leetcode.com/problems/permutations-ii/description/
# Medium

from itertools import permutations
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 算是作弊=。=
        return list(permutations(nums))
