//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++

class Solution {
  public:
  void fun(int i,int n,string &d,vector<string>&t,vector<vector<string>>&v)
  {
      if(i==n){
          v.push_back(t);
          return;
      }
      for(int k=i;k<n;k++){
          string s=d.substr(i,k-i+1);
          if(s==string(s.rbegin(),s.rend())){
              t.push_back(s);
          fun(k+1,n,d,t,v);
          t.pop_back();
          }
      }
  }
    vector<vector<string>> allPalindromicPerms(string s) {
        // code here
        int n=s.size();
        vector<string>t;
        vector<vector<string>>v;
        fun(0,n,s,t,v);
        return v;
        
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        string S;
        
        cin>>S;

        Solution ob;
        vector<vector<string>> ptr = ob.allPalindromicPerms(S);
        
        for(int i=0; i<ptr.size(); i++)
        {
            for(int j=0; j<ptr[i].size(); j++)
            {
                cout<<ptr[i][j]<<" ";
            }
            cout<<endl;
        }
    }
    return 0;
}
// } Driver Code Ends