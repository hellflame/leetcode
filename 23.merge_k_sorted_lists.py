# coding=utf8
# https://leetcode.com/problems/merge-k-sorted-lists/description/
# Hard

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        tmp = []
        for i in lists:
            while i:
                tmp.append(i.val)
                i = i.next

        if not tmp:
            # 如果所有链表为空链表，tmp不会添加任何元素，则不会存在tmp[0]
            return None

        # 之后的步骤，与单链表排序如出一辙
        tmp.sort()
        
        head = ans = ListNode(tmp[0])
        for i in range(len(tmp) - 1):
            head.val = tmp[i]
            head.next = ListNode(tmp[i + 1])
            head = head.next
        return ans


