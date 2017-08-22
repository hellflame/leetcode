# coding=utf8
# https://leetcode.com/problems/length-of-last-word/description/
# Easy

import re
regs = re.compile("([a-zA-Z]{1,})")
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = regs.findall(s)
        if result:
            return len(result[-1])
        return 0

"""
使用正则，确保仅仅匹配字母
虽然也有人使用下面的方法：

class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.strip().split(' ')[-1])

但是这样的话，跟测试用例返回的结果不一致，比如
hello world666
whatever!!!?
等

(但是提交的时候不会出现这些例子就是了=。=)

"""

