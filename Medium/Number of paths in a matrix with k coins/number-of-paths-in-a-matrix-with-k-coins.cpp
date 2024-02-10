//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
public:
 int fun(int i,int j,int s,vector<vector<int>>& nums,int k,vector<vector<vector<int>>> &dp,int n)
 {  
      if(i>n-1 || j>n-1 ||s>k)return 0;
     if(i==n-1 && j==n-1){
        //  cout<<s<<" "<<k<< endl;
         s=s+nums[i][j];
         if(s==k){
            //  cout<<"hi"<<" ";
            return 1;
            //  return 1;
         }
         else return 0;
     }
    
     if(dp[i][j][s]!=-1){;
             return dp[i][j][s];}
     
        int m=fun(i+1,j,s+nums[i][j],nums,k,dp,n);
        int c=fun(i,j+1,s+nums[i][j],nums,k,dp,n);
        return dp[i][j][s]=m+c;
 }
    
    long long numberOfPath(int n, int k, vector<vector<int>> arr){
        
        // Code Here
        long long c=0;
            vector<vector<vector<int> > > dp(
        n+1, vector<vector<int> >(n+1, vector<int>(200,-1)));

        return fun(0,0,0,arr,k,dp,n);
        
        
    }
};


//{ Driver Code Starts.

int main()
{
    Solution obj;
    int i,j,k,l,m,n,t;
    cin>>t;
    while(t--)
    {
        cin>>k>>n;
        vector<vector<int>> v(n, vector<int>(n, 0));
        for(i=0;i<n;i++)
            for(j=0;j<n;j++)
                cin>>v[i][j];
        cout << obj.numberOfPath(n, k, v) << endl;
    }
}
// } Driver Code Ends