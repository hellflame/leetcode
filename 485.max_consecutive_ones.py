# coding=utf8
# https://leetcode.com/problems/max-consecutive-ones/#/description
# Easy

# C Version
"""

int m = 0, count = 0, i;
    for(i = 0;i < numsSize; i++){
        if(nums[i]){
            count ++;
        }else{
            if(m < count){
                m = count;
            }
            count = 0;
        }
    }
    if(m < count){
        m = count;
    }
    return m;

"""

def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    m = 0
    for i in nums:
        if i:
            count += 1
            if m < count:
                m = count
        else:
            count = 0
            
    return m



