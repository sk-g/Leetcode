
//234. Palindrome Linked List

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
    bool isPalindrome(ListNode* head) {
        if(head == NULL || head->next == NULL) return true;
        return find(head,head->next)!=NULL?true:false;
    }
    ListNode* find(ListNode* head,ListNode* nex) {
        
        //If only one element
        if(nex==NULL) return head;
        
        //If you reach the last element
        if(nex->next==NULL)
            return head->val==nex->val ? head->next : NULL;
        
        //Recursively call till you reach last element.
        //As soon as you reach the last element, Just return the next of the head
        //So that previous calls can use that refernce and compare with the second last and so on
        
        ListNode* checkhead = find(head,nex->next);
        
        if(checkhead==NULL) return NULL;

        return checkhead->val==nex->val?checkhead->next:NULL;
        
    }
	    
};