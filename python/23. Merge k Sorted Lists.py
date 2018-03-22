#23. Merge k Sorted Lists

"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
Multiple approaches. Read solution section.

Most intuitive is to build sorted array of linked lists and then form one merged LL
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return lists
        self.numbers = []
        head = dummy = ListNode(10)
        for l in lists:
            while l:
                self.numbers.append(l.val)#creating array with LL vals
                l = l.next
        for i in sorted(self.numbers):#sort the array and build new LL
            dummy.next = ListNode(i)
            dummy = dummy.next
        return head.next