/*
In this challenge, you must first implement a queue using two stacks. Then process queries, where each query is one of the following

types:

    1: Enqueue element into the end of the queue.
    2: Dequeue the element at the front of the queue.
    3: Print the element at the front of the queue.

Input Format

The first line contains a single integer,
, denoting the number of queries.
Each line of the subsequent lines contains a single query in the form described in the problem statement above. 
All three queries start with an integer denoting the query , but only enqueue query is followed by an additional space-separated value,
 denoting the value to be enqueued.
*/
#include <cmath>
#include <cstdio>
#include <vector>
#include <stack>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n; 
    cin>>n;
    int a,b;
    stack<int> x,y;
    for (int i=0; i<n; i++){
        cin>>a;
        if (a==1){
            cin>>b;
            x.push(b);
        } else if (a==2){
            if (!y.empty()){y.pop();}
            else{
                while(!x.empty()){
                    b=x.top();
                    y.push(b);
                    x.pop();
                }
                y.pop();
            }
        } else {
            if (!y.empty()){cout<<y.top()<<endl;}
            else{
                while(!x.empty()){
                    b = x.top();
                    y.push(b);
                    x.pop();
                }
                cout<<y.top()<<endl;
            }
        }

    }
    return 0;
}
