//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
public:
    vector<int> recamanSequence(int n){
        // code here
        map<int,int>m;
        vector<int>v;
        v.push_back(0);
        for (int i=1;i<n;i++)
        {
            int c=v[v.size()-1]-i;
            int d=v[v.size()-1]+i;
            if(c>0 && m.find(c)==m.end()){
                v.push_back(c);
                m[c]=1;
            }
            else{
                v.push_back(d);
                m[d]=1;
            }
        }
        return v;
        
        
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        
        Solution ob;
        vector<int> ans = ob.recamanSequence(n);
        for(int i = 0;i < n;i++)
            cout<<ans[i]<<" ";
        cout<<"\n";
    }
    return 0;
}
// } Driver Code Ends