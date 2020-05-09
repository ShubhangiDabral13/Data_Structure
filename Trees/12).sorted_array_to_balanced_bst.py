"""
Time Complexity: O(n)
T(n) = 2T(n/2) + C
  T(n) -->  Time taken for an array of size n
   C   -->  Constant (Finding middle of array and linking root to left
                      and right subtrees take constant time)

"""
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


def array_bst(arr):
    if not arr:
        return None
    mid = (len(arr))//2
    root = Node(arr[mid])

    root.left = array_bst(arr[:mid])
    root.right = array_bst(arr[mid + 1:])

    return root


def preorder(node):
    if node != None:
        print(node.data)
        preorder(node.left)
        preorder(node.right)


arr = [1, 2, 3, 4, 5, 6, 7]
root = array_bst(arr)
print ("PreOrder Traversal of constructed BST ")
preorder(root)

"""
output:-
PreOrder Traversal of constructed BST
4
2
1
3
6
5
7

Constructed balanced BST is
  4
 /  \
 2   6
/ \ / \
1 3 5 7
"""
