"""
Time Complexity: O(n)
Auxiliary Space : O(1) if Function Call Stack size is not considered, otherwise O(n)
"""

INT_MAX = 4294967296
INT_MIN = -4294967296

class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

def checkbst(root):
    return (isbst(root,INT_MIN,INT_MAX))

def isbst(root,mini,maxi):

    if root is None:
        return True

    if root.value < mini or root.value > maxi:
        return False

    return((isbst(root.left, mini,root.value -1)) and (isbst(root.right,root.value + 1,maxi)))


root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

if (checkbst(root)):
    print("Is BST")
else:
    print( "Not a BST")
