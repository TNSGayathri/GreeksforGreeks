//{ Driver Code Starts
// driver

#include <bits/stdc++.h>
using namespace std;

/* Linked list Node */
struct Node {
    int data;
    struct Node* next;
    Node(int x) {
        data = x;
        next = NULL;
    }
};

struct Node* buildList(int size)
{
    int val;
    cin>> val;
    
    Node* head = new Node(val);
    Node* tail = head;
    
    for(int i=0; i<size-1; i++)
    {
        cin>> val;
        tail->next = new Node(val);
        tail = tail->next;
    }
    
    return head;
}

void printList(Node* n)
{
    while(n)
    {
        cout<< n->data << " ";
        n = n->next;
    }
    cout<< endl;
}


// } Driver Code Ends
/* node for linked list:

struct Node {
    int data;
    struct Node* next;
    Node(int x) {
        data = x;
        next = NULL;
    }
};

*/

class Solution
{
    public:
    //Function to add two numbers represented by linked list.
    struct Node *rev(struct Node *head)
    {
        Node *pr=NULL;
        Node *ne=NULL;
        Node *c=head;
        while(c)
        {
            ne=c->next;
            c->next=pr;
            pr=c;
            c=ne;
        }
        head=pr;
        return head;
    }
    struct Node* addTwoLists(struct Node* first, struct Node* second)
    {
        // code here
        Node *t1=rev(first);
        Node *t2=rev(second);
        Node *h1=NULL;
        int c=0;
        while (t1!=NULL && t2!=NULL){
            int k=t1->data+t2->data+c;
            c=k/10;
            Node *n=new Node(k%10);
            n->next=h1;
            h1=n;
            t1=t1->next;
            t2=t2->next;
        }
        while(t1!=NULL){
            int k=t1->data+c;
            c=k/10;
            Node *n=new Node(k%10);
            n->next=h1;
            h1=n;
            t1=t1->next;
            
        }
        while(t2!=NULL)
        {
            int k=t2->data+c;
            c=k/10;
            Node *n=new Node(k%10);
            n->next=h1;
            h1=n;
            t2=t2->next;
        }
        if(c!=0){
            Node *n=new Node(c);
            n->next=h1;
            h1=n;
        }
        return h1;
        
    }
};


//{ Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n, m;
        
        cin>>n;
        Node* first = buildList(n);
        
        cin>>m;
        Node* second = buildList(m);
        Solution ob;
        Node* res = ob.addTwoLists(first,second);
        printList(res);
    }
    return 0;
}

// } Driver Code Ends