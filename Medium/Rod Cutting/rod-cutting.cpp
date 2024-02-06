//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution{
  public:
  int dp[100001];
  int fun(int cuts[],int n){
    if(n==0){
return dp[n]=0;
    }
    if(dp[n]!=-1)
    {
        return dp[n];
    }
    int maxans=INT_MIN;
    int ans=0;
    for (int i=0;i<n;i++){
       int  l=i+1;
       ans=cuts[i]+fun(cuts,n-l);
        dp[n]=max(ans,dp[n]);
    }
        
    return dp[n];
}
    int cutRod(int price[], int n) {
        //code here
        memset(dp,-1,sizeof(dp));
        return fun(price,n);
        
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int a[n];
        for (int i = 0; i < n; i++) 
            cin >> a[i];
            
        Solution ob;

        cout << ob.cutRod(a, n) << endl;
    }
    return 0;
}
// } Driver Code Ends