//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;
 

// } Driver Code Ends
/*You are required to complete this method*/

class Solution
{
    public:
    int dp[1000][1000];
    int mod=1e9+7;
    int fun(string s, string t, int i,string k ,int j){
        if(k==t){
            
        return dp[i][j]=1;}
        if(i==s.size())return dp[i][j]=0;
        if(dp[i][j]!=-1)return dp[i][j]%mod;
        int d=0,e=0;
if(s[i]==t[j]){
    // cout<<s[i]<<t[j]<<" ";
        d+=fun(s,t,i+1,k+s[i],j+1);
}
        e+=fun(s,t,i+1,k,j);
        return dp[i][j]=(d+e)%mod;
    }
    int subsequenceCount(string s, string t)
    {
    // int c=0;
    memset(dp, -1, sizeof(dp));
    string k="";
    return fun(s,t,0,k,0);
    }
};
 



//{ Driver Code Starts. 

//  Driver code to check above method
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		string s;
		string tt;
		cin>>s;
		cin>>tt;
		
		Solution ob;
		cout<<ob.subsequenceCount(s,tt)<<endl;
		
		
	}
  
}
// } Driver Code Ends