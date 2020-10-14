class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value


def insert(root,node):
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


# Given a non-empty binary search tree, return the node
# with minum  value found in that tree. Note that the
# entire tree does not need to be searched
def minvalue(node):
    current = node

    if current.left != None:
        current = current.left

    return current

# Given a binary search tree and a value, this function
# delete the value and returns the new root
def deletenode(root,value):

    if root == None:
        return root

    # If the value to be deleted is smaller than the root's
    # value then it lies in  left subtree
    if root.value > value:
        root.left = deletenode(root.left,value)


     # If the value to be delete is greater than the root's value
    # then it lies in right subtree
    elif root.value < value:
        root.right = deletenode(root.right,value)


    # If value is same as root's value,  then this is the node
    # to be deleted
    else:

         # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp


        elif root.right is None:
            temp = root.left
            root = None
            return  temp

        # Node with two children: Get the inorder successor
        # (smallest in the right subtree)
        temp = minvalue(root.right)

        # Copy the inorder successor's content to this node
        root.value = temp.value

        # Delete the inorder successor
        root.right = deletenode(root.right,temp.value)


    return root


# Driver program to test above functions
""" Let us create following BST
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80 """

root = Node(50)
#root = insert(root, Node(50))
insert(root, Node(30))
insert(root, Node(20))
insert(root, Node(40))
insert(root, Node(70))
insert(root, Node(60))
insert(root, Node(80))

print ("Inorder traversal of the given tree")
inorder(root)

print("\nDelete 20")
root = deletenode(root, 20)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 30")
root = deletenode(root, 30)
print("Inorder traversal of the modified tree")
inorder(root)


print("\nDelete 50")
root = deletenode(root, 50)
print("Inorder traversal of the modified tree")
inorder(root)

"""
Output:-
Inorder traversal of the given tree
20
30
40
50
60
70
80

Delete 20
Inorder traversal of the modified tree
30
40
50
60
70
80

Delete 30
Inorder traversal of the modified tree
40
50
60
70
80

Delete 50
Inorder traversal of the modified tree
40
60
70
80
"""
