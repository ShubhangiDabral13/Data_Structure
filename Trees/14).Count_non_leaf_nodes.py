#Time complixity of code is 0(N) Where N is total number of nodes.
class Node:
    def __init__(self,data):
        self.value = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.head = None

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


def non_leaf_nodes(root):

    if root == None:
        return 0

    if root.left == None and root.right == None:
        return 0

    return 1 + non_leaf_nodes(root.left) + non_leaf_nodes(root.right)

    return 0



r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))

print("The total number of non leaf nodes are ",non_leaf_nodes(r))

"""
Output:
The total number of non leaf nodes are  3
"""
