class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> seen;
        unordered_set<int> result;
        for(int num :nums1){
                seen.insert(num);
            }
        for(int num:nums2){
            if(seen.find(num)!=seen.end()){
                result.insert(num);
            }
        }
        return vector<int> (result.begin(),result.end());
    }
};