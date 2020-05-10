class Node:
    def __init__(self,data):
        self.data = data
        self.left =  None
        self.right = None

def print_path(path,j):
    for i in range(j,len(path)):
        print(path[i] , end = " ")
    print()

def printallpath(path,root,k):
    if (not root):
        return
    path.append(root.data)

    printallpath(path,root.left,k)
    printallpath(path,root.right ,k)
    f = 0
    for i in range(len(path) -1,-1,-1):
        f += path[i]

        if k == f:
            print_path(path,i)

    path.pop(-1)

def printKPath(root, k):

    path =[]
    printallpath(path,root, k)

# Driver Code
if __name__ == '__main__':

    root = Node(1)
    root.left = Node(3)
    root.left.left = Node(2)
    root.left.right = Node(1)
    root.left.right.left = Node(1)
    root.right = Node(-1)
    root.right.left = Node(4)
    root.right.left.left = Node(1)
    root.right.left.right = Node(2)
    root.right.right = Node(5)
    root.right.right.right = Node(2)

    k = 5
    printKPath(root, k)

"""
Output:-
3 2
3 1 1
1 3 1
4 1
1 -1 4 1
-1 4 2
5
1 -1 5
"""    
