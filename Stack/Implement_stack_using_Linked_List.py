class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

class Stack:
    def __init__(self):
        self.head = None


    def isempty(self):
        if self.head == None:
            return  True

        else:
            False


    def push(self,data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node

        else:
            new_node.next = self.head.next
            self.head = new_node


            # Remove element that is the current head (start of the stack)
    def pop(self):

        if self.isempty():
            return None

        else:
            # Removes the head node and makes
            #the preceeding one the new head
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    def peek(self):

        if self.isempty():
            return None

        else:
            return self.head.data

    # Prints out the stack
    def display(self):

        iternode = self.head
        if self.isempty():
            print("Stack Underflow")

        else:

            while(iternode != None):

                print(iternode.data,"->",end = " ")
                iternode = iternode.next
            return

# Driver code
MyStack = Stack()

MyStack.push(11)
MyStack.push(22)
MyStack.push(33)
MyStack.push(44)

# Display stack elements
MyStack.display()

# Print top element of stack
print("\nTop element is ",MyStack.peek())

# Delete top elements of stack
MyStack.pop()
MyStack.pop()

# Display stack elements
MyStack.display()

# Print top element of stack
print("\nTop element is ", MyStack.peek())
