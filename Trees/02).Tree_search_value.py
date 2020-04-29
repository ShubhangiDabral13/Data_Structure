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

# A utility function to search a given key in BST
def search(root,value):

    if root is None:

        print("The tree is empty")
        return

    elif root.value == value:

        print("the {} is present at {}".format(value,root))
        return

    elif root.value < value:

        search(root.right,value)

    elif root.value > value:
        search(root.left,value)

    else:
        
        print("{} is not present".format(value))
        return

r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))
inorder(r)
print(search(r,20))
