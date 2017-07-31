# coding=utf8
# https://leetcode.com/problems/reverse-vowels-of-a-string/#/description
# Easy

# C Version
"""

int is_vowel(char a){
    if(a == 'a' || a == 'e' || a == 'i' || a == 'o' || a == 'u' || a == 'A' || a == 'E' || a == 'I' || a == 'O' || a == 'U'){
        return 1;
    }
    return 0;
}

char* reverseVowels(char* s) {
    int size = strlen(s), left = 0, right = size - 1, left_v, right_v;
    char tmp;
    while(left < right){
        left_v = is_vowel(s[left]);
        right_v = is_vowel(s[right]);
        
        if(left_v && right_v){
            tmp = s[left];
            s[left] = s[right];
            s[right] = tmp;
            left ++;
            right --;
        }
        if(!right_v){
            right --;
        }
        if(!left_v){
            left ++;
        }
    }
    return s;
}

"""

def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    target = list(s)
    left = 0
    right = len(target) - 1
    check = {
        'a': True,
        'e': True,
        'i': True,
        'o': True,
        'u': True,
        'A': True,
        'E': True,
        'I': True,
        'O': True,
        'U': True
    }
    while left < right:
        if check.get(target[left]) and check.get(target[right]):
            target[left], target[right] = target[right], target[left]
            left += 1
            right -= 1
        elif not check.get(target[left]):
            left += 1
        elif not check.get(target[right]):
            right -= 1
            
    return "".join(target)
    

if __name__ == '__main__':
    print reverseVowels("hellflame is fine")



