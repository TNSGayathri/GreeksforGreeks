//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
public:
    void fun1(vector<int>&v,int n, int t){
            v.push_back(n);
            if(n==t){return;}
            
            fun1(v,n+5,t);
            
    }
    int fun(vector<int> &v,int n,int t){
        v.push_back(n);
          if(n<=0){
              return t;
          }
          t=n;
          fun(v,n-5,t);
    }
    vector<int> pattern(int N){
        // code here
                vector<int>v;
        if(N<=0)
        {
            v.push_back(N);
            return v;
        }

        int t=N;
        int t1=fun(v,N,t);
        fun1(v,t1,t);
        return v;
        
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int N;
        cin>>N;
        
        Solution ob;
        vector<int> ans = ob.pattern(N);
        for(int u: ans)
            cout<<u<<" ";
        cout<<"\n";
    }
    return 0;
}
// } Driver Code Ends