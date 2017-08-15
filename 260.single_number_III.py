# coding=utf8
# https://leetcode.com/problems/single-number-iii/description/
# Medium

# O(n)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        save = set()
        for i in nums:
            if i not in save:
                save.add(i)
            else:
                save.remove(i)
        return list(save)

