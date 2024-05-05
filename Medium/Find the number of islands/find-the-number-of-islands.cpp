//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
    void bfs(int n,int m,vector<vector<int>> &vis,vector<vector<char>> &grid ,int i,int j)
    {
        vis[i][j]=1;
        queue<pair<int,int>>q;
        q.push({i,j});
        while(!q.empty()){
            int row=q.front().first;
            int col=q.front().second;
            q.pop();
            for(int neirow=-1;neirow<=1;neirow++)
            {
                for(int neicol=-1;neicol<=1;neicol++)
                {
                    int nerow=row+neirow;
                    int necol=col+neicol;
                    if(nerow>=0 && nerow<n && necol>=0 && necol<m && grid[nerow][necol]=='1' && !vis[nerow][necol])
                    {
                        vis[nerow][necol]=1;
                        q.push({nerow,necol});
                    }
                }
            }
        }
        
    }
  public:
    // Function to find the number of islands.
    
    int numIslands(vector<vector<char>>& grid) {
        // Code here
        int n=grid.size();
        int m=grid[0].size();
        int cnt=0;
        vector<vector<int>>vis(n,vector<int>(m,0));
        for(int i=0;i<n;i++)
        {
            for (int j=0;j<m;j++)
            {
                if(!vis[i][j] && grid[i][j]=='1'){
                    cnt++;
                    bfs(n,m,vis,grid,i,j);
                }
                
            }
        }
        return cnt;
    }
};

//{ Driver Code Starts.
int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int n, m;
        cin >> n >> m;
        vector<vector<char>> grid(n, vector<char>(m, '#'));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> grid[i][j];
            }
        }
        Solution obj;
        int ans = obj.numIslands(grid);
        cout << ans << '\n';
    }
    return 0;
}
// } Driver Code Ends