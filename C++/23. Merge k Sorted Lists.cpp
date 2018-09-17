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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        multimap<int,ListNode*> mp;
        for(auto node: lists){
            if(node!=NULL)
                mp.insert(make_pair(node->val,node));
        }
        ListNode *ret = NULL;
        ListNode *p = NULL;
        while (!mp.empty()) {
            multimap<int, ListNode*>::iterator it = mp.begin();
            if (ret == NULL) {
                ret = it->second;
                p = ret;
            } else {
                p->next = it->second;
                p = p->next;
            }
            if (it->second->next != NULL) {
                mp.insert(make_pair(it->second->next->val, it->second->next));
            }
            mp.erase(it);
        }               
        return ret;
    }
};