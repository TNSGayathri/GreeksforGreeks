//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
public:
void fun(int n,vector<int> &l){
    if(n==0){
        return ;
    }
    if(n>=2000){
        l.push_back(2000);
        fun(n-2000,l);
    }
    else if(n>=500){
        l.push_back(500);
        fun(n-500,l);
    }
    else if(n>=200){
        l.push_back(200);
        fun(n-200,l);
    }
    else if(n>=100){
        l.push_back(100);
        fun(n-100,l);
    }
    else if(n>=50){
        l.push_back(50);
        fun(n-50,l);
    }
    else if(n>=20){
        l.push_back(20);
        fun(n-20,l);
    }
    else if(n>=10){
        l.push_back(10);
        fun(n-10,l);
    }
    else if(n>=5){
        l.push_back(5);
        fun(n-5,l);
    }
    else if(n>=2){
        l.push_back(2);
        fun(n-2,l);
    }
    else if(n>=1){
        l.push_back(1);
        fun(n-1,l);
    }
}
    vector<int> minPartition(int N)
    {
        // code hereif(N+
        vector<int> l;
        fun(N,l);
        return l;
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
        vector<int> numbers = ob.minPartition(N);
        for(auto u: numbers)
            cout<<u<<" ";
        cout<<"\n";
    }
    return 0;
}
// } Driver Code Ends