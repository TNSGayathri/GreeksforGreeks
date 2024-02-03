//{ Driver Code Starts
// Program to check if linked list is empty or not
#include<iostream>
using namespace std;
const long long unsigned int MOD = 1000000007;

/* Link list Node */
struct Node
{
    bool data;
    struct Node* next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
    
};


// } Driver Code Ends
/* Below global variable is declared in code for modulo arithmetic
const long long unsigned int MOD = 1000000007; */

/* Link list Node/
struct Node
{
    bool data;   // NOTE data is bool
    Node* next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
    
}; */
#include <math.h>
#include <stdio.h>
class Solution
{
    public:
        // Should return decimal equivalent modulo 1000000007 of binary linked list
        int mod=1000000007;
        int po(int n,int c){
            int ans=1;
            while(c>0){
            if(c%2!=0){
                c=c-1;
                ans=((ans%mod)*(n%mod))%mod;
            }
            else{
                c=c/2;
                n=((n%mod)*(n%mod))%mod;
            }
            }
            return ans%mod;
        }
        long long unsigned int decimalValue(Node *head)
        {
           // Your Code Here
           
           Node *p=NULL;
           Node *n=NULL;
           Node *c=head;
           while (c){
               n=c->next;
               c->next=p;
               p=c;
               c=n;
           }
           head=p;
           Node *t=head;
        //   while (t!=NULL){
        //       cout<<t->data<<" ";
        //       t=t->next;
        //   }
        //   t = head;
           long long c1=1;
           unsigned long long int s=0;
          while (t!=NULL){
              if(t->data){
              s=(s%mod+c1%mod)%mod;
            //   cout<<po(2,c1)<<" ";}
              }
              c1 = (c1%mod*2%mod)%mod;
              t=t->next;
               
          }
           return s%mod;
           
        }
};




//{ Driver Code Starts.

void append(struct Node** head_ref, struct Node **tail_ref, bool new_data)
{

    struct Node* new_node = new Node(new_data);
    
    if (*head_ref == NULL)
       *head_ref = new_node;
    else
       (*tail_ref)->next = new_node;
    *tail_ref = new_node;
}


bool isEmpty(struct Node *head);

/* Driver program to test above function*/
int main()
{
    bool l;
    int i, n, T;

    cin>>T;

    while(T--){
    struct Node *head = NULL,  *tail = NULL;

        cin>>n;
        for(i=1;i<=n;i++)
        {
            cin>>l;
            append(&head, &tail, l);
        }
        Solution obj;
        cout << obj.decimalValue(head) << endl;
    }
    return 0;
}
// } Driver Code Ends