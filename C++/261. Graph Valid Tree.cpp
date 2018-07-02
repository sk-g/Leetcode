//261. Graph Valid Tree

class Solution {
public:
    bool validTree(int n, vector<pair<int, int>>& edges) {
        vector<int> nodes(n,0);
        for(int i=0;i<nodes.size();++i){
            nodes[i] = i;
        }
        for(int i=0;i<edges.size();++i){
            int root1 = edges[i].first;
            int root2 = edges[i].second;
            while(nodes[root1]!=root1)
                root1 = nodes[root1];
            while(nodes[root2]!=root2)
                root2 = nodes[root2];
            if(root1==root2)
                return false;
            nodes[root2] = root1;
        }
        return  edges.size() == n-1;
    }
};