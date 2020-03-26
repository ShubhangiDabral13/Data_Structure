"""
Given a value, delete the first occurrence of this value in linked list.
To delete a node from linked list, we need to do following steps.
1) Find previous node of the node to be deleted.
2) Change the next of previous node to the next of given node  .
3) Free memory for the node to be deleted.
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next  = None

class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def deletenode(self,key):
        temp = self.head
        if temp == None:
            print("Linked list does not have any node")
            return
        elif temp.data == key:
            temp = None
            return
        else:
            while(temp != None):
                if(temp.data == key):
                    break
                prev = temp
                temp = temp.next
            prev.next =  temp.next

    def display(self):
        temp = self.head
        if temp == None:
            print("There is no node in linked list")
            return
        else:
            while(temp != None):
                print(temp.data,end=" ")
                temp = temp.next

ll = Linked_List()
ch = 0
while(ch != 4):
    print("""Enter 1 to insert a node at front in Linked_List
    Enter 2 to delete node for a particular key value
    Enter 3 to print the linked List
    Enter 4 to to quit """)
    ch = int(input())
    if ch == 1:
        print("Enter the data you want to insert in the linked list")
        a = int(input())
        ll.insert(a)

    elif ch == 2:
        a = int(input("Enter the key value whose node you want to delete"))
        ll.deletenode(a)

    elif ch == 3:
        ll.display()

    elif ch == 4:
        print("We will quit")

    else:
        print("Wrong choice")
