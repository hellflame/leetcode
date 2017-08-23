# coding=utf8
# https://leetcode.com/problems/basic-calculator-ii/description/
# Medium


class Solution(object):
    def to_suffix(self, s):
        s1 = []
        s2 = []
        weight = {'+': 0, '-': 0, '*': 1, '/': 1}
        tmp = ''
        for i in s:
            if i.isdigit():
                tmp += i
            else:
                s1.append(tmp)
                tmp = ''
                if not i == ' ':
                    while s2 and weight[s2[-1]] >= weight[i]:
                        s1.append(s2.pop())
                    s2.append(i)
        s1.append(tmp)
        while s2:
            s1.append(s2.pop())
        return s1[::-1]
    
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = self.to_suffix(s)
        tmp = []
        while True:
            if not len(s) and len(tmp) == 1:
                return int(tmp[0])
            elif s[0].isdigit() or s[0].startswith('-') and not s[0] == '-':
                return int(s[0])
            t = s.pop()
            if t.isdigit() or t.startswith('-') and not t == '-':
                tmp.append(t)
            else:
                if t == '*':
                    # print s, tmp
                    s.append(str(int(tmp.pop()) * int(tmp.pop())))
                    # print s, tmp
                elif t == '-':
                    s.append(str( - int(tmp.pop()) + int(tmp.pop())))
                elif t == '+':
                    s.append(str(int(tmp.pop()) + int(tmp.pop())))
                elif t == '/':
                    a = float(tmp.pop())
                    b = float(tmp.pop())
                    s.append(str(int(b / a)))
