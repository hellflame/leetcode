# coding=utf8
# https://leetcode.com/problems/integer-to-english-words/description/
# Hard

# not hard to think but too many special condition

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        thousands = ['Thousand', 'Million', 'Billion']
        digit_1 = {
            '0': '',
            '1': 'One',
            '2': 'Two',
            '3': 'Three',
            '4': 'Four',
            '5': 'Five',
            '6': 'Six',
            '7': 'Seven',
            '8': 'Eight',
            '9': 'Nine',
            '10': 'Ten',
            '11': 'Eleven',
            '12': 'Twelve',
            '13': 'Thirteen',
            '14': 'Fourteen',
            '15': 'Fifteen',
            '16': 'Sixteen',
            '17': 'Seventeen',
            '18': 'Eighteen',
            '19': 'Nineteen'
        }
        digit_2 = {
            '2': 'Twenty',
            '3': 'Thirty',
            '4': 'Forty',
            '5': 'Fifty',
            '6': 'Sixty',
            '7': 'Seventy',
            '8': 'Eighty',
            '9': 'Ninety'
        }
        if not num:
            return 'Zero'
        
        num = str(num)
        index = 3
        target = []
        result = ''
        check = num[-3:]
        while check:
            tmp = ''
            if len(check) == 3:
                tmp = digit_1[check[0]]
                if int(check[0]):
                    tmp += ' Hundred '
                if check[1] == '1':
                    tmp += digit_1[check[1] + check[2]]
                elif check[1] == '0':
                    tmp += digit_1[check[2]]
                else:
                    tmp += digit_2[check[1]] + ' ' + digit_1[check[2]]
            elif len(check) == 2:
                if check[0] == '1':
                    tmp = digit_1[check]
                elif check[0] == '0':
                    tmp = digit_1[check[1]]
                else:
                    tmp = digit_2[check[0]] + ' ' + digit_1[check[1]]
            elif len(check) == 1:
                tmp = digit_1[check]
            
            target.append(tmp.strip())
            check = num[-3 - index: - index]
            index += 3
        # print target
        length = len(target)
        if length == 1:
            return target[0]
        index = 0
        for i in target[::-1]:
            result += i
            if length - index  - 2>= 0 and i:
                result += ' ' + thousands[length - index - 2] + ' '
            index += 1
        # print result 
            
        return result.strip()

