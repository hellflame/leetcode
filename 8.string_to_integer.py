# coding=utf8
# https://leetcode.com/problems/string-to-integer-atoi/description/
# Medium

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = ''
        legal = {'-', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        str = str.strip()
        for i in str:
            if i in legal:
                s += i
            else:
                break
        if not s:
            return 0
        try:
            print s
            if '-' in s and not s.startswith("-"):
                result = int(s[0:s.index('-')])
            else:
                result = int(s)
        except:
            return 0
        
        if result > 2147483647:
            return 2147483647
        if result < -2147483648:
            return -2147483648
        return result

