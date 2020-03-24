#Linked List Implementation to create a list which consist of 3 nodes.

#Class Node
class Node:
    #To Initialize object
    def __init__(self,data):
        self.data = data
        self.next = None


#Class to create link between nodes
class Linked_List:
    def __init__(self):
        self.head = None

    #To print the data of the nodes
    def print(self):
        temp = self.head
        while(temp):
            print("{}".format(temp.data),end = " ")
            temp = temp.next


# Start with the empty lis
link = Linked_List()


first = Node(1)
second = Node(2)
third = Node(3)
link.head = first
# Link first node with second
first.next = second
# Link second node with the third node
second.next = third
third.next = None
link.print()
