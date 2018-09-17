/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
// public:
//     unordered_map<int,bool> m;
    
//     bool findTarget(TreeNode* root, int k) {
        
//        if(root==NULL) return false;
        
//        if(m.find(root->val)!=m.end())
//            return true;   
        
//         m[k - root->val] = true;

//         return findTarget(root->left,k) || findTarget(root->right,k);
//     }
// };
// class Solution {
public:
    unordered_map<int,int> map;
    bool findTarget(TreeNode* root, int k) {
        if(root == NULL)
            return false;
        
        if(map.find(root->val)!=map.end())
            return true;
        map[k-root->val] = root->val;
        return findTarget(root->left,k) ||findTarget(root->right,k);
        
    }
};