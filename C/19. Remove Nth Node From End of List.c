/*
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
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    if(head==NULL) return head;
    if(head->next==NULL) return NULL;
    int a=0;
    struct ListNode *t=head, *prev=head, *temp=head;
    while(t!=NULL){
        a+=1;
        t=t->next;
    }
    #n=a-n;
    #printf("%d,%d",head->next->val,n);
    if(a==n){
        prev=head;
        head=prev->next;
        free(prev);
    }
    else{
        while(a>n){
        	prev=temp;
        	temp=temp->next;
        	a--;
    	}

    	prev->next=temp->next;
    	free(temp);
    }
    return head;
   
}