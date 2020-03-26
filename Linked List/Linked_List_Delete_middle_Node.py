"""
Alogorithm to delete the middle node of the Linked_List
1). Declare 3 pointers slow_temp,temp,prev_temp.
2). Traverse the Linked List.
3). Move temp by two and slow_temp by one and while traversing track of previous of slow_temp storing it in prev_temp.
4). When temp reaches end of the Linked List, slow_temp reaches middle of the Linked List.
5). Delete the middle node.
"""

#Class Node to create a Node
class Node:
    def __init__(self,data):
        self.data = data
        self.next  = None
#Class Linked_List to link different nodes all together
class Linked_List:
    def __init__(self):
        self.head = None

    #Add the node to the linked list
    def insert(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    #To delete middle node from the linked list
    def del_mid_node(self):
        temp = self.head
        slow_temp = self.head
        if temp == None:
            print("Linked list is empty")
            return
        elif temp.next == None:
            temp = None
            return
        else:
            while(temp != None and temp.next != None):
                prev_temp = slow_temp
                slow_temp = slow_temp.next
                temp = temp.next.next
            prev_temp.next = slow_temp.next

    #To display the element of the linked list
    def display(self):
        temp = self.head
        if temp == None:
            print("There is no node in linked list")
            return
        else:
            while(temp != None):
                print(temp.data,end=" ")
                temp = temp.next

#Creating instance of the class Linked_List
ll = Linked_List()
ch = 0
while(ch != 4):
    print("""Enter 1 to insert a node at front in Linked_List
    Enter 2 to delete middle node in a linked list
    Enter 3 to print the linked List
    Enter 4 to to quit """)
    ch = int(input())
    if ch == 1:
        print("Enter the data you want to insert in the linked list")
        a = int(input())
        ll.insert(a)

    elif ch == 2:
        ll.del_mid_node()

    elif ch == 3:
        ll.display()

    elif ch == 4:
        print("We will quit")

    else:
        print("Wrong choice")
