//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++

class Solution{
    public:
    void fun(int i,int j,int n,vector<vector<int>> m,vector<string> &v,string f)
    {
        if(i>=n ||j>=n ||i<0 || j<0){
           return ;
       }
       if(m[i][j]==0 || m[i][j]==-1){
           return ;
       }
       if(i==n-1 && j==n-1){
           v.push_back(f);
           return ;
       }
       
       
          
       m[i][j]=-1;
       fun(i+1,j,n,m,v,f+"D");
        fun(i,j+1,n,m,v,f+"R");
        fun(i,j-1,n,m,v,f+"L");
        fun(i-1,j,n,m,v,f+"U");
        m[i][j]=1;
       
       
       
       
    }
    vector<string> findPath(vector<vector<int>> &m, int n) {
        // Your code goes here
        string f;
        vector<string> v;
        fun(0,0,n,m,v,f);
        return v;
    }
};

    


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<vector<int>> m(n, vector<int> (n,0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> m[i][j];
            }
        }
        Solution obj;
        vector<string> result = obj.findPath(m, n);
        sort(result.begin(), result.end());
        if (result.size() == 0)
            cout << -1;
        else
            for (int i = 0; i < result.size(); i++) cout << result[i] << " ";
        cout << endl;
    }
    return 0;
}
// } Driver Code Ends