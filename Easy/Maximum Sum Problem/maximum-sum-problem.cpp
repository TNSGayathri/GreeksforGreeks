//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
    public:
    int fun(int n){
        if(n<=11) return n;
        int m=n;
        int m1=fun(n/2);
        int m2=fun(n/3);
        int m3=fun(n/4);
        int c=m1+m2+m3;
        return max(m,c);
        
    }
        int maxSum(int n)
        {
            //code her.
            return fun(n);
            
        }
};

//{ Driver Code Starts.
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        Solution ob;
        cout<<ob.maxSum(n)<<"\n";
    }
    return 0;
}
// } Driver Code Ends