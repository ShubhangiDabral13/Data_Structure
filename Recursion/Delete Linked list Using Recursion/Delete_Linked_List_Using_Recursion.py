class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_List:
    #Constructor to Initialize it's parameter
    def __init__(self):
        self.head = None

    #To insert the node
    def insert(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    #To delete the node from the end
    def delete_linked_list(self):
        if self.head == None:
            return
        self.head = self.head.next
        self.delete_linked_list()

    def printList( self) :
        temp = self.head
        if temp == None:
            print("List is empty")
            return
        while (temp != None):
            print(temp.data, end = " ")
            temp = temp.next
        print("\n")

link = Linked_List()
ch = 0
while ch != 4:
    print("""Enter 1 to insert number
    Enter 2 to delete linked list
    Enter 3 to display linked List
    Enter 4 to quit""")

    ch = int(input())
    if ch == 1:
        a = int(input("Enter the number u want to insert"))
        link.insert(a)

    elif ch == 2:
        link.delete_linked_list()

    elif ch == 3:
        link.printList()

    elif ch == 4:
        print("We will quit")

    else:
        print("Wrong choice")
