# coding=utf8
# https://leetcode.com/problems/rotate-array/#/description
# Easy

# C Version
"""
// O(kn)

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


if __name__ == '__main__':
    import time
    start = time.time()
    rotate(range(2048), 500)
    print time.time() - start




