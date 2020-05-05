"""
Program to count leaf nodes in a binary tree

Algorithm:-
getLeafCount(node)
1) If node is NULL then return 0.
2) Else If left and right child nodes are NULL return 1.
3) Else recursively calculate leaf count of the tree using below formula.
    Leaf count of a tree = Leaf count of left subtree + Leaf count of right subtree

Time Complexity: O(n)
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
def getLeafCount(root):
    if root  == None:
        return 0
    elif root.right == None and root.left == None:
        return  1
    else:
        return (getLeafCount(root.right) + getLeafCount(root.left))


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Leaf count of the tree is %d" %(getLeafCount(root)))
