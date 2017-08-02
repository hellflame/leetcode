# codeing=utf8
# https://leetcode.com/problems/validate-ip-address/description/
# Medium

import re

class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        v4_regs = re.compile("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}")
        v6_regs = re.compile("[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}")
        
        v4 = v4_regs.findall(IP)
        v6 = v6_regs.findall(IP)
        if len(v4) == 1 and v4[0] == IP:
            for i in IP.split("."):
                if int(i) > 255:
                    return 'Neither'
                elif not str(int(i)) == i:
                    return 'Neither'
            return "IPv4"
        elif len(v6) == 1 and v6[0] == IP:
            return "IPv6"
        
        return 'Neither'
                

