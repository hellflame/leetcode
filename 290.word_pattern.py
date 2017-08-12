# coding=utf8
# https://leetcode.com/problems/word-pattern/description/
# Easy

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not len(str.split(" ")) == len(pattern):
            return False
        return len(set(zip(pattern, str.split(" ")))) == len(set(pattern)) == len(set(str.split(" ")))

