# coding=utf8
# https://leetcode.com/problems/reverse-string/#/description
# Easy

# C Version
"""

char* reverseString(char* s) {
    int size = strlen(s), i, pos, mid = size / 2;
    char tmp;
    for(i=0; i < mid; i++){
        tmp = s[i];
        pos = size - i - 1;
        s[i] = s[pos];
        s[pos] = tmp;
    }
    return s;
}

"""

def reverseString(s):
    """
    :type s: str
    :rtype: str
    """
    length = len(s)
    s = list(s)
    for i in range(length / 2):
        s[i], s[length - i - 1] = s[length - i - 1], s[i]
    
    return "".join(s)

if __name__ == '__main__':
    print reverseString("hellflame")



