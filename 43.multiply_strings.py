# coding=utf8
# https://leetcode.com/problems/multiply-strings/description/
# Medium

import numpy
import re

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # 卷积 得到的结果就是没有进位的乘法结果，剩下的工作就是进位了
        result = numpy.convolve([int(x) for x in num1], [int(x) for x in num2])
        index = len(result) - 1
        carry = 0
        while index >= 0:
            result[index] += carry
            carry = result[index] / 10
            result[index] %= 10
            index -= 1
        if carry:
            result = str(carry) + ''.join([str(x) for x in result])
        else:
            result = ''.join([str(x) for x in result])
        
        # 去除前导 '0'
        if not result.startswith("0"):
            return result
        else:
            regs = re.compile("0{1,}(\d*)")
            tmp = regs.findall(result)[0]
            if not tmp:
                return "0"
            return tmp

