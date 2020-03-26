"""
Given a singly linked list and a position, delete a linked list node at the given position.
Example:

Input: position = 1, Linked List = 8->2->3->1->7
Output: Linked List =  8->3->1->7

Input: position = 0, Linked List = 8->2->3->1->7
Output: Linked List = 2->3->1->7
"""

#Class Node to create a node
class Node:
    def __init__(self,data):
        self.data = data
        self.next  = None

#Class Linked_List to link different nodes together
class Linked_List:
    #Constructor to Initialize all parameters
    def __init__(self):
        self.head = None

    #To insert new value to the node
    def insert(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    #To delete a node at a particular position
    def delete_node_by_pos(self,pos):
        if self.head == None:
            print("linked list is empty")
            return
        else:
            temp = self.head
            #To find previous node
            for i in range(pos-1):
                temp = temp.next
                if(temp == None):
                    break
            #If position is more than number of nodes in linked List
            if temp == None or temp.next == None:
                return
            else:
                new_temp = temp.next.next
            temp.next = new_temp

    #To print all the elements in Linked_List.
    def display(self):
        temp = self.head
        if temp == None:
            print("There is no node in linked list")
            return
        else:
            while(temp != None):
                print(temp.data,end=" ")
                temp = temp.next

#Creating the instance of the class Linked_List
ll = Linked_List()
ch = 0
while(ch != 4):
    print("""Enter 1 to insert a node at front in Linked_List
    Enter 2 to delete node by position
    Enter 3 to print the linked List
    Enter 4 to to quit """)
    ch = int(input())
    if ch == 1:
        print("Enter the data you want to insert in the linked list")
        a = int(input())
        ll.insert(a)

    elif ch == 2:
        a = int(input("Enter the position at which you want to delete the node"))
        ll.delete_node_by_pos(a)

    elif ch == 3:
        ll.display()

    elif ch == 4:
        print("We will quit")

    else:
        print("Wrong choice")
