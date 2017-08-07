# coding=utf8
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# Easy

# solution one
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        checked = {}
        i = 0
        while i < len(numbers) and numbers[0] + numbers[i] <= target:
            tmp = target - numbers[i]
            if tmp in checked:
                return checked[tmp] + 1, i + 1
            checked[numbers[i]] = i
            i += 1

# solution two
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        right = len(numbers) - 1
        while numbers[0] + numbers[right] > target:
            right -= 1
            
        checked = {}
        i = 0
        while i <= right:
            tmp = target - numbers[i]
            if tmp in checked:
                return checked[tmp] + 1, i + 1
            checked[numbers[i]] = i
            i += 1

# solution three
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while True:
            s = numbers[left] + numbers[right]
            if s > target:
                right -= 1
            elif s < target:
                left += 1
            else:
                return left + 1, right + 1




