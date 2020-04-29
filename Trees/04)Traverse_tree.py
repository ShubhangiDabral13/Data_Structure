class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

def insert(root, value):
    if root == None:
        return Node(value)

    elif value < root.value:
        root.left = insert(root.left , value)

    elif value > root.value:
        root.right = insert(root.right , value )

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value )
        inorder(root.right)

def postorder(root):
    if root :
        postorder(root.left)
        postorder(root.right)
        print(root.value)


def preorder(root):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)

root =None
root = insert(root ,1)
root = insert(root,2)
root = insert(root,3)
root =insert(root,4)
root = insert(root,5)
print ("Preorder traversal of binary tree is")
preorder(root)

print( "\nInorder traversal of binary tree is")
inorder(root)

print ("\nPostorder traversal of binary tree is")
postorder(root)
