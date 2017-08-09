# coding=utf8
# https://leetcode.com/problems/valid-parentheses/description/
# Easy

# python 中的数组用作栈
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        symbols = {'(', '[', '{'}
        for i in s:
            if i in symbols:
                stack.append(i)
            else:
                if not stack:
                    return False
                if i == ')':
                    if not stack.pop() == '(':
                        return False
                elif i == ']':
                    if not stack.pop() == '[':
                        return False
                elif i == '}':
                    if not stack.pop() == '{':
                        return False
        return not stack
                        
            