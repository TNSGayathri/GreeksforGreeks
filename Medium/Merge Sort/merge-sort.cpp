//{ Driver Code Starts
#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;



/* Function to print an array */
void printArray(int arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}


// } Driver Code Ends
class Solution
{
    public:
    void merge(int a[], int l, int m, int r)
    {
         // Your code here
         int i=l,k=0,j=m+1;
         int temp[r-l+1];
         while(i<=m && j<=r){
             if(a[i]<a[j]){
                 temp[k++]=a[i++];
             }
             else{
                 temp[k++]=a[j++];
             }
         }
         while(i<=m){
             temp[k++]=a[i++];
         }
         while(j<=r){
             temp[k++]=a[j++];
         }
         k=0;
         for (int i=l;i<=r;i++){
             a[i]=temp[k++];
         }
    }
    public:
    void mergeSort(int arr[], int l, int r)
    {
        //code here
        int mid=l+(r-l)/2;
        if(l>=r) return ;
        mergeSort(arr,l,mid);
        mergeSort(arr,mid+1,r);
        merge(arr,l,mid,r);
    }
};

//{ Driver Code Starts.


int main()
{
    int n,T,i;

    scanf("%d",&T);

    while(T--){
    
    scanf("%d",&n);
    int arr[n+1];
    for(i=0;i<n;i++)
      scanf("%d",&arr[i]);

    Solution ob;
    ob.mergeSort(arr, 0, n-1);
    printArray(arr, n);
    }
    return 0;
}
// } Driver Code Ends