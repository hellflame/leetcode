# coding=utf8
# https://leetcode.com/problems/add-strings/description/
# Easy

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1 = len(num1)
        len2 = len(num2)
        
        if len1 > len2:
            carry = 0
            result = [int(x) for x in num1]
            index = len1 - 1
            i = -1
            while index >= 0 and i >= -len2:
                
                result[index] = result[index] + int(num2[i]) + carry
                carry = result[index] / 10
                result[index] %= 10
                
                index -= 1
                i -= 1
        else:
            carry = 0
            result = [int(x) for x in num2]
            index = len2 - 1
            i = -1
            while index >= 0 and i >= -len1:
                
                result[index] = result[index] + int(num1[i]) + carry
                carry = result[index] / 10
                result[index] %= 10
                
                index -= 1
                i -= 1
        if carry:
            while index >= 0:
                result[index] += carry
                carry = result[index] / 10
                result[index] %= 10
                index -= 1
        if carry:
            return str(carry) + ''.join(str(x) for x in result)
        return ''.join(str(x) for x in result)
                    
        