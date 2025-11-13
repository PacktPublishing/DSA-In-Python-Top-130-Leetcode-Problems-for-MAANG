class Solution {
public:
    int minAddToMakeValid(string s) {
        int count = 0, ans = 0;
        for(int i = 0; i < s.size(); i++) {
            if (s[i] == '(') {
                count++;
            }
            else {
                count--;
            }
            if (count < 0) {
                ans += 1;
                count++;
            }
        }
        ans += count;
        return ans;
    }
};
