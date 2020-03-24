#Program to insert nodes at different location on linked list.
#Class to create the Node
class Node:
    #To Initialize object
    def __init__(self,data):
        self.data = data #To Initialize the data
        self.next = None# To Initialize next pointer

#Class to create link between nodes
class Linked_List:
    def __init__(self):
        #To Initialize next pointer to NULL
        self.head = None

    #To insert node at the front of the linked List
    def insert_at_front(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head = new_node

    # To insert the node at the given position
    def insert_at_given_pos(self,pos,data):
        new_node = Node(data)
        temp = self.head
        count = 0
        while(count == pos):
            temp = temp.next
            count += 1
        new_node.next = temp.next
        temp.next = new_node

    #To insert node at the end of linked list
    def insert_at_end(self,data):
        new_node = Node(data)
        temp = self.head
        if temp is None:
            temp  = new_node
            return
        while(temp.next):
            temp = temp.next
        temp.next = new_node

    #To print the linked list
    def print(self):
        temp = self.head
        while(temp):
            print("{}".format(temp.data),end = " ")
            temp = temp.next


#To create a Linked_List instance
link = Linked_List()

link.insert_at_front(23)
link.insert_at_front(10)
link.insert_at_front(20)
link.insert_at_end(11)
link.insert_at_given_pos(2,45)
link.print()
