//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
	public:
	void fun(string S,string s,vector<string>&v,vector<int>&fr){
	    if(S.size()==s.size())
	    {if(!count(v.begin(),v.end(),s)){
	        v.push_back(s);
	        return ;}
	    }
	    for(int i=0;i<S.size();i++){
	        if(fr[i]==0)
	        {
	            fr[i]=1;
	            fun(S,s+S[i],v,fr);
	            fr[i]=0;
	        }
	    }
	    
	}
		vector<string>find_permutation(string S)
		{
		    // Code here there
		    sort(S.begin(),S.end());
		    string s="";
		    vector<int>fr(S.size(),0);
		    vector<string>v;
		    fun(S,s,v,fr);
		    return v;
		}
};



//{ Driver Code Starts.
int main(){
    int t;
    cin >> t;
    while(t--)
    {
	    string S;
	    cin >> S;
	    Solution ob;
	    vector<string> ans = ob.find_permutation(S);
	    sort(ans.begin(),ans.end());
	    for(auto i: ans)
	    {
	    	cout<<i<<" ";
	    }
	    cout<<"\n";
    }
	return 0;
}

// } Driver Code Ends