//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{

	public:
	long long dp[1000000];
	long long fun(vector<int>&A,int M,int v)
	{
	    if(v==0){
	        return 0;
	    }
	    long long ans=INT_MAX;
	    if(dp[v]!=-1)return dp[v];
	    for (int i=0;i<M;i++){
	        if(A[i]<=v){
	            ans=min(ans,1+fun(A,M,v-A[i]));
	        }
	    }
	    return dp[v]=ans;
	}
	int minCoins(vector<int> &coins, int M, int V) 
	{ 
	    // Your code goes here
	    memset(dp,-1,sizeof(dp));
	    long long c=fun(coins,M,V);
	    if(c==INT_MAX)return -1;
	    return c;
	    
	} 
	  
};

//{ Driver Code Starts.
int main() 
{
   
   
   	int t;
    cin >> t;
    while (t--)
    {
        int v, m;
        cin >> v >> m;

        vector<int> coins(m);
        for(int i = 0; i < m; i++)
        	cin >> coins[i];

      
	    Solution ob;
	    cout << ob.minCoins(coins, m, v) << "\n";
	     
    }
    return 0;
}

// } Driver Code Ends