"""
Time Complexity: Time complexity is O(n) 
"""
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def lca(root,n1,n2,v):

    if root is None:
        return None

    if root.data == n1:
        v[0] = True
        return  root

    if root.data == n2:
        v[1] = True
        return root

    left_lca = lca(root.left,n1,n2,v)
    right_lca = lca(root.right ,n1,n2,v)

    if left_lca and right_lca  :
        return root

    return left_lca if left_lca is not None else right_lca


def find(root,k):
    if root is None:
        return False
    if(root.data == k or find(root.left,k) or find(root.right,k)):
        return True

    return False


def findLCA(root, n1, n2):

    v = [False, False]
    ans = lca(root, n1, n2, v)


    if (v[0] and v[1] or v[0] and find(ans, n2) or v[1] and find(ans, n1)):
        return ans

    return None



# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

ans = findLCA(root, 4, 5)

if ans is not None:
    print ("LCA(4, 5) = ",ans.data)
else :
    print ("Keys are not present")

ans = findLCA(root, 4, 10)
if ans is not None:
    print ("LCA(4,10) = ", ans.data)
else:
    print ("Keys are not present")


"""
Output:-
LCA(4, 5) =  2
Keys are not present

"""
