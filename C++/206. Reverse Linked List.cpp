/*
206. Reverse Linked List
DescriptionHintsSubmissionsDiscussSolution
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?


Difficulty:Easy
Total Accepted:368.4K
Total Submissions:772.1K

*/



/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    //iterative
    ListNode* reverseList(ListNode* head) {
        if(head == NULL||head->next == NULL) return head;
        ListNode* pre = NULL;
        ListNode* cur = head;
        while(cur!=NULL){
            ListNode* temp = cur->next;
            cur->next = pre;
            pre = cur;
            cur = temp;
        }
        return pre;
    }
};