# coding=utf8
# https://leetcode.com/problems/sort-list/description/
# Medium


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        # 转换为列表排序，然后生成目标链表
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        tmp.sort()
        head = ans = ListNode(tmp[0])
        for i in range(len(tmp) - 1):
            head.val = tmp[i]
            head.next = ListNode(tmp[i + 1])
            head = head.next
        return ans
            
            
            