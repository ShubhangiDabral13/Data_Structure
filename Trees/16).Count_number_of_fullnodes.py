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


def count_full_nodes(root):
    if root == None:
        return 0
    elif root.left != None and root.right != None:
        return 1 + count_full_nodes(root.left) + count_full_nodes(root.right)

    return count_full_nodes(root.left) + count_full_nodes(root.right)


r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))

print("The total number of full nodes are ",count_full_nodes(r))


"""
Output:
The total number of full nodes are  3
"""
