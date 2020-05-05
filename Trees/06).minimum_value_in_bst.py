"""
Find the node with minimum value in a Binary Search Tree
Time complexity = 0(N)
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

def min_value(root):
    current = root
    while(current.left != None):
        current = current.left

    return current.data

# Driver program
root = None
root = insert(root,4)
root = insert(root,2)
root = insert(root,1)
root = insert(root,3)
root = insert(root,6)
root = insert(root,5)

print ("\nMinimum value in BST is %d"  %(min_value(root)))
