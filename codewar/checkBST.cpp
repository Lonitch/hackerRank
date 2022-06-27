/* 
Given the root node of a binary tree, can you determine if it's also a binary search tree?

Complete the function in your editor below, which has 1 parameter: 
    a pointer to the root of a binary tree. It must return a boolean denoting whether or not the binary tree is a binary search tree. 
    You may have to write one or more helper functions to complete this challenge.

Hidden stub code will pass a root argument to the function below. Complete the function to solve the challenge. 

The Node struct is defined as follows:
	struct Node {
		int data;
		Node* left;
		Node* right;
	}
*/
    bool BSTutil(Node* node, int min, int max){
        if (node==nullptr){
            return true;
        }
        if (node->data<min || node->data>max){
            return false;
        } else {
            return BSTutil(node->left, min, node->data-1) && BSTutil(node->right, node->data+1, max);
        }
    }
	bool checkBST(Node* root) {
		int min = -2147483647;
        int max = 2147483647;
        return BSTutil(root, min, max);
	}