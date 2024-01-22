//{ Driver Code Starts
#include<bits/stdc++.h>

using namespace std;

struct Node
{
    int data;
    Node* next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
};


void print(Node *root)
{
    Node *temp = root;
    while(temp!=NULL)
    {
        cout<<temp->data<<" ";
        temp=temp->next;
    }
}



// } Driver Code Ends
/*

The structure of linked list is the following

struct Node
{
    int data;
    Node* next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
};
*/
class Solution
{
    public:
    Node *rev(Node *head)
    {
      Node *c=head;
        Node *p=NULL,*n=NULL;
        while(c)
        {
            n=c->next;
            c->next=p;
            p=c;
            c=n;
        }
        head=p;
        return head;
    }
    Node *compute(Node *head)
    {
        // your code goes here
       Node *h1=rev(head);
       Node *t=h1;
       while(t)
       {
          while(t->next!=NULL && t->data>t->next->data)
          {
              t->next=t->next->next;
            //   t=t->next;
            //   cout<<t->data<<" ";
          }
          t=t->next;
       }
       Node *h2=rev(h1);
       return h2;
        
        
    }   
};
   


//{ Driver Code Starts.

int main()
{
    int T;
	cin>>T;

	while(T--)
	{
		int K;
		cin>>K;
		struct Node *head = NULL;
        struct Node *temp = head;

		for(int i=0;i<K;i++){
		    int data;
		    cin>>data;
			if(head==NULL)
			    head=temp=new Node(data);
			else
			{
				temp->next = new Node(data);
				temp = temp->next;
			}
		}
        Solution ob;
        Node *result = ob.compute(head);
        print(result);
        cout<<endl;
    }
}

// } Driver Code Ends