# coding=utf8
# https://leetcode.com/problems/merge-two-sorted-lists/description/
# Easy

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 and l2:
            if l1.val < l2.val:
                start = l1
                l1 = l1.next
            else:
                start = l2
                l2 = l2.next
        elif l1:
            return l1
        elif l2:
            return l2
        else:
            return None
        
        result = start
        while True:
            if l1 and l2:
                if l1.val < l2.val:
                    result.next = l1
                    l1 = l1.next
                    result = result.next
                else:
                    result.next = l2
                    result = result.next
                    l2 = l2.next
            elif l1:
                result.next = l1
                l1 = None
            elif l2:
                result.next = l2
                l2 = None
            else:
                break
        return start
        
