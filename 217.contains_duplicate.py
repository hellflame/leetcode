# coding=utf8
# https://leetcode.com/problems/contains-duplicate/#/description
# Easy

def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    a = set(nums)
    return not len(a) == len(nums)

