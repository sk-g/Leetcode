"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.

Difficulty: Medium

Solution : 

Only trick - nth from end => (length-n)th from the beginning

so two pass solution : 
1. get lenght
2. delete node.

Straightforward once you get the trick
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        list_len = 0
        d = head
        while d:
            d = d.next
            list_len +=1
        
        if list_len == n:
            head = head.next
            return head
        
        #to_remove = (list_len-n)-1
        
        prev,temp = head,head
        while list_len > n:
            prev = temp
            temp = temp.next
            list_len -=1
        prev.next = temp.next
        del temp
        return head

## fastest solution : 

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        
        slow = fast = dummy
        
        for _ in range(n):
            fast = fast.next
            
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        
        return dummy.next        