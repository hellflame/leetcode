# coding=utf8
# https://leetcode.com/problems/rotate-array/#/description
# Easy

# C Version
"""
// O(kn) 时间复杂度与 K 成正比

void rotate(int* nums, int numsSize, int k) {
    int tmp, i;
    k = k % numsSize;
    while(k > 0){
        tmp = nums[numsSize - 1];
        for(i = numsSize - 1;i > 0 ; i --){
            nums[i] = nums[i - 1];
        }
        nums[0] = tmp;
        k --;
    }
}

"""

def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    leng = len(nums)
    k = k % leng
    while k > 0:
        tmp = nums[leng - 1]
        for i in reversed(range(1, leng)):
            nums[i] = nums[i - 1]
        nums[0] = tmp
        k -= 1
    # print nums

def rotate_inner(nums, k):
    # 原地排序，O(n)，时间复杂度与 K 无关
    length = len(nums)
    k = length - k % length    
    for i in range(k / 2):
        nums[i], nums[k - i - 1] = nums[k - i - 1], nums[i]

    for i in range(k, k + (length - k) / 2):
        nums[i], nums[length - i + k - 1] = nums[length - i + k - 1], nums[i]

    for i in range(length / 2):
        nums[i], nums[length - i - 1] = nums[length - i - 1], nums[i]

    return nums


def rotate_outer(nums, k):
    k = len(nums) - k % len(nums)
    return nums[k:] + nums[:k]


if __name__ == '__main__':
    import time
    length = 1000000
    start = time.time()
    rotate(range(length), 16)
    print "rorate: \t", time.time() - start

    start = time.time()
    rotate_inner(range(length), 16)
    print "rotate-inner: \t", time.time() - start

    start = time.time()
    rotate_outer(range(length), 16)
    print "rotate-outer: \t", time.time() - start

    
    




