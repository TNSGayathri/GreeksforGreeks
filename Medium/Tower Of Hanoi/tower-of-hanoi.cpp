//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends
class Solution{
    public:
    // You need to complete this function

    // avoid space at the starting of the string in "move disk....."
    void Movedisk(int N,int from,int to,int aux,long long &c){
        if(N>0)
        {
           Movedisk(N-1,from,aux,to,c);
           cout<<"move disk "<<N<<" from rod "<<from<< " to rod "<<to<<endl;
           c+= 1;
           Movedisk(N-1,aux,to,from,c);
        }
    }
    long long toh(int N, int from, int to, int aux) {
        // Your code here
        long long c=0;
        Movedisk(N,from,to,aux,c);
        return c;
    }

};

//{ Driver Code Starts.

int main() {

    int T;
    cin >> T;//testcases
    while (T--) {
        
        int N;
        cin >> N;//taking input N
        
        //calling toh() function
        Solution ob;
        
        cout << ob.toh(N, 1, 3, 2) << endl;
    }
    return 0;
}



// } Driver Code Ends