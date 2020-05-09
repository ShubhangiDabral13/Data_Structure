"""
Let T be a rooted tree. The lowest common ancestor between two nodes n1 and n2 is defined as the lowest node in
T that has both n1 and n2 as descendants
Time complexity of above solution is O(h) where h is height of tree.
"""

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def lca(root,n1,n2):
    while root:
        if n1 < root.data and n2 < root.data :
            root = root.left
        elif n1 > root.data and n2 > root.data:
            root = root.right

        else:
            break
    return root

# Let us construct the BST shown in the figure
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

n1 = 10 ; n2 = 14
t = lca(root, n1, n2)
print ("LCA of %d and %d is %d" %(n1, n2, t.data))

n1 = 14 ; n2 = 8
t = lca(root, n1, n2)
print ("LCA of %d and %d is %d" %(n1, n2 , t.data))

n1 = 10 ; n2 = 22
t = lca(root, n1, n2)
print ("LCA of %d and %d is %d" %(n1, n2, t.data))


"""
output:-
LCA of 10 and 14 is 12
LCA of 14 and 8 is 8
LCA of 10 and 22 is 20
"""
