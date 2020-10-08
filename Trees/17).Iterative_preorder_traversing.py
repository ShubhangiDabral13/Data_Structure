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


def preorder(root):

    s = []
    ans = []
    s.append(root)

    while s!= []:
        val = s.pop()
        ans.append(val.value)
        if val.right!= None:
            s.append(val.right)
        if val.left != None:
            s.append(val.left)

    return ans



r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))

print(preorder(r))

"""
Output
[50,30,20,40,70,60,80]
"""
