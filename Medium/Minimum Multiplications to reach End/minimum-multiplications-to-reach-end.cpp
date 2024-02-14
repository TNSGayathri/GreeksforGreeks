//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++
#include <queue>
class Solution {
  public:
   int mod=1e5;
    int minimumMultiplications(vector<int>& arr, int start, int end) {
        // code here
        if(start==end)return 0;
        queue<pair<int,int>>q;
        vector<int>v(100000,0);
        q.push({start,0});
        int f=1;
        while (!q.empty()){
            int c=q.front().first;
            int c1=q.front().second;
            q.pop();
            for(int i=0;i<arr.size();i++)
            {
                int k=(c*arr[i])%mod;
                if(v[k]!=1)
                {
                    q.push({k,c1+1});
                    v[k]=1;
                }
                if(k==end){
                    return c1+1;
                }
            }
            
        }
        return -1;
    }
    // return 0;
};


//{ Driver Code Starts.

int main() {

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        int start, end;
        cin >> start >> end;
        Solution obj;
        cout << obj.minimumMultiplications(arr, start, end) << endl;
    }
}

// } Driver Code Ends