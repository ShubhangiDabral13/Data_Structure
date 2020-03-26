"""Aglorithm to delete the starting node:-
1)If head is None then there is no node to delete ,so return from the function
2)if there is one node then poin the head to NULL
3)If there are more then one node then point the head to the node'next node  which head the head was previously pointing
"""
#Class to create a node
class Node:
    def __init__(self,data):
        self.data = data
        self.next  = None

#To link all the node in linked list
class Linked_List:
    #Constructor to Initialize the node's parameter
    def __init__(self):
        self.head = None

    #To insert a new Node
    def insert(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    #To delete a node from beginning
    def delete_start_node(self):
        if self.head == None:
            print("There is no node to delete")
            return
        else:
            self.head = self.head.next

    #To display element of linked List
    def display(self):
        temp = self.head
        if temp == None:
            print("There is no node in linked list")
            return
        else:
            while(temp != None):
                print(temp.data,end=" ")
                temp = temp.next

#To create an instance pf the class Linked_List
ll = Linked_List()
ch = 0
while(ch != 4):
    print("""Enter 1 to insert a node at front in Linked_List
    Enter 2 to delete a starting node
    Enter 3 to print the linked List
    Enter 4 to to quit """)
    ch = int(input())
    if ch == 1:
        print("Enter the data you want to insert in the linked list")
        a = int(input())
        ll.insert(a)

    elif ch == 2:
        ll.delete_start_node()

    elif ch == 3:
        ll.display()

    elif ch == 4:
        print("We will quit")

    else:
        print("Wrong choice")
