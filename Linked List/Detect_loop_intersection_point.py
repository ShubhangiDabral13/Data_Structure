#Class Node is being created
class Node:
    def __init__(self,val):
        self.val = val
        self.next = next


class Linked_List:
    def __init__(self):
        #To Initialize next pointer to NULL
        self.head = None

    #To insert node at the front of the linked List
    def insert(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head = new_node


    def detect_intersection_point(self):
        #Try to find whether loop exist.If exist then assign true to loop else loop will be False.
        slow,fast = self.head,self.head
        loop = False
        while(fast!= None and fast.next != None):
            slow = slow.next
            fast = fast.next.next

            if fast == slow :
               loop = True
               break



        #find the node where loop is being formed
        if loop:
            slow = self.head
            while(slow != fast):
                slow = slow.next
                fast = fast.next

            print("The intersection is present at {}".format(slow))

        else:
            print("Loop not detected")




llist = Linked_List()
llist.insert(20)
llist.insert(4)
llist.insert(15)
llist.insert(10)

# Create a loop for testing
llist.head.next.next.next.next = llist.head
llist.detect_intersection_point()
