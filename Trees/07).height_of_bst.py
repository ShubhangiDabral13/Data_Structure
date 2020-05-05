"""
Write a Program to Find the Maximum Depth or Height of a Tree
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


def height(root):

    if root == None:
        return 0

    else:
        lheight = height(root.left)
        rheight = height(root.right)

        if(lheight > rheight):
            return  lheight + 1
        else:
            return rheight + 1


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print ("Height of tree is %d" %(height(root)))
