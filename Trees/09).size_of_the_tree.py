"""
Write a program to Calculate Size of a tree | Recursion

Algorithm:-
size(tree)
1. If tree is empty then return 0
2. Else
     (a) Get the size of left subtree recursively  i.e., call
          size( tree->left-subtree)
     (a) Get the size of right subtree recursively  i.e., call
          size( tree->right-subtree)
     (c) Calculate size of the tree as following:
            tree_size  =  size(left-subtree) + size(right-
                               subtree) + 1
     (d) Return tree_size

Time Complexity = 0(N)
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def insert(root,value):
    if root == None:
        return Node(value)
    elif root.data > value:
        root.left  = insert(root.left,value )
    else:
        root.right = insert(root.right , value)

    return root

def size_tree(root):
    if root == None:
        return 0
    else:
        return(size_tree(root.left) + 1 + size_tree(root.right))



# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left  = Node(4)
root.left.right = Node(5)

print ("Size of the tree is %d" %(size_tree(root)))                 
