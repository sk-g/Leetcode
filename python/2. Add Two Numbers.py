#2. Add Two Numbers
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Pretty straight forward. Only keep in mind the carry.

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 212 ms 43.49%
        # first base cases:
        # if either of the
        # list is empty, return
        # the other one
        # if both are empty return none
        if not l1:
            return l2
        if not l2:
            return l1
        if not l2 and not l1:
            return none
        # else init a carry propagator
        carry = 0
        # instantiate new linked list
        root = n = ListNode(1)
        # while there is something
        # to be added, ll1 or ll2 
        # or the carry itself
        # do:
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:# while you can still traverse LL1
                v1 = l1.val# get current node value
                l1 = l1.next# get next node
            if l2:# while you can still traverse LL2
                v2 = l2.val
                l2 = l2.next
            
            
            val = v1 + v2 + carry # add numbers + carry if any
            carry = val//10 # if sum > 10, get the quotient as carry
            val %= 10# this is the rem or second digit of sum
            n.next = ListNode(val)# push that into new LL
            n = n.next# move to next node
        return root.next#return the head of new LL