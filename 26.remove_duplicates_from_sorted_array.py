# coding=utf8
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/#/description
# Easy

# C Version
"""

int removeDuplicates(int* nums, int numsSize) {
    if(!numsSize){
        return 0;
    }
    int left = 0, right = 0;
    while(right < numsSize){
        if(nums[right] == nums[left]){
            right ++;
        }else{
            left ++;
            nums[left] = nums[right];
            right ++;
        }
    }
    return left + 1;
}

"""

# Python 字符串不允许原地操作
