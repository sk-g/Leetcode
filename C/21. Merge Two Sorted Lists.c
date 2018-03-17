/* 21. Merge Two Sorted Links
*
* Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
* Logic: deal with end cases first.
*       recursively move values based on which is greater
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void MoveNode(struct ListNode** destRef, struct ListNode** sourceRef){
    struct ListNode* newNode=*sourceRef;
    if(newNode != NULL){
    *sourceRef = newNode->next;
    newNode->next = *destRef;
    *destRef = newNode;
    }
}
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode dummy;
    struct ListNode* tail=&dummy;
    dummy.next=NULL;
    while(1){
        if(l1==NULL){
            tail->next=l2;
            break;
        }
        else if (l2==NULL){
            tail->next=l1;
            break;
        }
        /*if(l1->val<l2->val)
            MoveNode(&(tail->next),&l1);
        else
            MoveNode(&(tail->next),&l2);*/
        (l1->val>l2->val) ? MoveNode(&(tail->next),&l2) : MoveNode(&(tail->next),&l1);
            tail=tail->next;
    }
    return(dummy.next);
}