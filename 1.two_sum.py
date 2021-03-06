# coding=utf8
# https://leetcode.com/problems/two-sum/description/
# Easy

# O(n)
# 字典记录可与当前值匹配获得目标值的位置
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            x = nums[i]
            if target - x in d:
                return d[target - x], i
            d[x] = i

# O(n2)
# 普通的依次加和比较
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        length = len(nums)
        while i < length - 1:
            j = i + 1
            while j < length:
                if nums[i] + nums[j] == target:
                    return i, j
                j += 1
            i += 1

