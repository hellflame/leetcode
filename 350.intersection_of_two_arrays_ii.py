# coding=utf8
# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
# Easy

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for i in nums1:
            if i in nums2:
                result.append(i)
                # 效率略低
                nums2.remove(i)
                
        return result

