# coding=utf8
# https://leetcode.com/problems/array-partition-i/#/description
# Easy

def arrayPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    sums = 0
    for i in nums[::2]:
        sums += i
    return sums