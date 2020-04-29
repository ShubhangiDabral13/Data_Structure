"""
Insertion of a value
A new value is always inserted at leaf. We start searching a value from root till we hit a leaf node.
Once a leaf node is found, the new node is added as a child of the leaf node.

         100                               100
        /   \        Insert 40            /    \
      20     500    --------->          20     500
     /  \                              /  \
    10   30                           10   30
                                              \
                                              40
"""
#class that represents an individual node in a BST
class Node:
    def __init__(self,value):
        self.right = None
        self.left = None
        self.value = value

#function to insert a new node with the given value
def insert(root ,node):
    if root is None:
        root = node
    else:
        if root.value > node.value:
            if root.left is None:
                root.left = node
            else:
                insert(root.left,node)
        else:
            if root.value < node.value:
                if root.right is None:
                    root.right = node
                else:
                    insert(root.right , node)

#function to do inorder tree traversal 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)


r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))
inorder(r)
