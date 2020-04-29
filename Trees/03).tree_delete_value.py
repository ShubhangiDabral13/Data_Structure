class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

def insert(root ,value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left , value)
    else:
        root.right = insert(root.right , value)

    return root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.value)
        inorder(root.right)


# Given a non-empty binary search tree, return the node
# with minum key value found in that tree. Note that the
# entire tree does not need to be searched
def minvaluenode(root):
    current = root
    # loop down to find the leftmost leaf
    while current.left != None:
        current = current.left
    return current

# Given a binary search tree and a key, this function
# delete the key and returns the new root
def delnode(root,value):

    if root == None:
        return root
    # If the key to be deleted is smaller than the root's
    # key then it lies in  left subtree
    elif value < root.value:
        root.left = delnode(root.left,value)
    # If the kye to be delete is greater than the root's key
    # then it lies in right subtree
    elif value > root.value:
        root.right = delnode(root.right, value)

    else:

        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp
        # Node with two children: Get the inorder successor
        # (smallest in the right subtree)
        temp = minvaluenode(root.right)

        # Copy the inorder successor's content to this node
        root.value = temp.value

         # Delete the inorder successor 
        root.right = delnode(root.right,temp.value)

    return root

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print ("Inorder traversal of the given tree")
inorder(root)

print ("\nDelete 20")
root = delnode(root, 20)
print ("Inorder traversal of the modified tree")
inorder(root)

print ("\nDelete 30")
root = delnode(root, 30)
print ("Inorder traversal of the modified tree")
inorder(root)

print ("\nDelete 50")
root = delnode(root, 50)
print ("Inorder traversal of the modified tree")
inorder(root)
