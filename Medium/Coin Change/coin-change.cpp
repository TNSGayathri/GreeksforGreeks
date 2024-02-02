//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    long long int dp[1002][1002];
    long long Fun(int ind,int sum,int coins[],int n){
        if(dp[ind][sum]!=-1)
          return dp[ind][sum];
        if(ind >= n){
            if(sum == 0)return 1;
            return 0;
        }
        long long a= 0,b = 0;
        
        a = Fun(ind+1,sum,coins,n);
        if(coins[ind]<=sum) {
        b = Fun(ind,sum-coins[ind],coins,n);
        }
        return dp[ind][sum]=a+b;
    }
    long long int count(int coins[], int N, int sum) {

        // code here.
        memset(dp,-1,sizeof(dp));
        return Fun(0,sum,coins,N);
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int sum, N;
        cin >> sum >> N;
        int coins[N];
        for (int i = 0; i < N; i++) cin >> coins[i];
        Solution ob;
        cout << ob.count(coins, N, sum) << endl;
    }

    return 0;
}


// } Driver Code Ends