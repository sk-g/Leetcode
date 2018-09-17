class Solution {
public:
    int calPoints(vector<string>& ops) {
        vector<int> rounds;
        for(int i = 0; i< ops.size(); ++i){
            if(ops[i] == "D"){
                rounds.push_back(rounds.back()*2);
            }
            else if(ops[i] == "+"){
                int x = rounds.size();
                rounds.push_back(rounds[x-1]+rounds[x-2]);
            }
            else if(ops[i] == "C"){
                rounds.pop_back();
            }
            else
                rounds.push_back(stoi(ops[i]));
        }
        return accumulate(rounds.begin(),rounds.end(),0);
    }
};
