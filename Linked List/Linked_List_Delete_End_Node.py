"""
1).If the first node is null or there is only one node, then return null
---if headNode == null then return null
---if headNode.nextNode == null then free head and return null
2).Create an extra space secondLast, and traverse the linked list till the second last node.
---while secondLast.nextNode.nextNode != null
      secondLast = secondLast.nextNode
delete the last node, i.e. the next node of second last node delete(secondLast.nextNode),and set the value of next of second last node to null.
"""

#Use to create a node
class Node:
    def __init__(self,data):
        self.data = data
        self.next  = None

#To connect node to a link List
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
    def delete_end_node(self):
        temp = self.head
        if temp is None:
            print("there is no node in linked list")
            return
        elif temp.next == None:
            temp = None
            return
        else:
            secondLast = temp
            while(secondLast.next.next != None):
                secondLast = secondLast.next
            secondLast.next = None
            return

    #To display element in Linked_List
    def display(self):
        temp = self.head
        if temp == None:
            print("There is no node in linked list")
            return
        else:
            while(temp != None):
                print(temp.data,end=" ")
                temp = temp.next

#To create instance of a classs
ll = Linked_List()
ch = 0
while(ch != 4):
    print("""Enter 1 to insert a node at front in Linked_List
    Enter 2 to delete the end node
    Enter 3 to print the linked List
    Enter 4 to to quit """)
    ch = int(input())
    if ch == 1:
        print("Enter the data you want to insert in the linked list")
        a = int(input())
        ll.insert(a)

    elif ch == 2:
        ll.delete_end_node()

    elif ch == 3:
        ll.display()

    elif ch == 4:
        print("We will quit")

    else:
        print("Wrong choice")
