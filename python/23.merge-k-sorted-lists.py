#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
from typing import *
from queue import PriorityQueue
from heapq import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwo(self, linked1: ListNode, linked2: ListNode) -> Optional[ListNode]:
        if not linked1: return linked2
        res = ListNode(0)
        dummy = res
        while linked1 and linked2:
            l1 = linked1.val
            l2 = linked2.val
            if l1 <= l2:
                dummy.next = linked1
                linked1 = linked1.next
            else:
                dummy.next = linked2
                linked2 = linked2.next
            dummy = dummy.next
        if linked1:
            dummy.next = linked1
            dummy = dummy.next
        elif linked2:
            dummy.next = linked2
            dummy = dummy.next
        return res.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:   return
        total = len(lists)
        interval = 1

        while interval < total:
            for i in range(0, total - interval, interval * 2):
                lists[i] = self.mergeTwo(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if total > 0 else None


# @lc code=end

