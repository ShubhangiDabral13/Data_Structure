"""
Algorithm to implement Queue using Stack:-
1.Take 2 Stacks, stack1 and stack2.
2.stack1 will be used a back of the Queue and stack2 will be used as front of the Queue.
3.Push() operation will be done on stack1, and  pop() operations will be done on stack2.
4.When pop() are called, check is stack2 is empty, if yes then move all the elements from stack1 and push them into
 stack2.
"""
#Class stack which consist of all the basic function of the stack
class Stack:
    #To  initialize a list named as stack
    def __init__(self):
        self.stack = []

    #Ton append the element to list
    def push(self,a):
        self.stack.append(a)

    #To remove the topmost element from stack
    def pop(self):
        return(self.stack.pop())

    #To get the size ot the list
    def get_size(self):
        return len(self.stack)

#Class queue which is used to implement queue using stack
class Queue:

    #To initialize two class Stack instance
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    #To get the size
    def get_size(self):
        return(self.get_size())

    #To push the element ins stack s1
    def enqueue(self,a):
        self.s1.push(a)

    def dequeue(self):
        if self.s1.stack == 0:
            print(" Stack is empty")
        else:
            for i in range(self.s1.get_size()):
                a = self.s1.stack.pop()
                self.s2.stack.append(a)
            res = self.s2.stack.pop()
            self.s1,self.s2 = self.s2,self.s1
            self.s1.stack = self.s1.stack[::-1]
            print("The deleted element is {}".format(a))

    #To display the element of stack.
    def display(self):
        print(self.s1.stack)

#Main function
q = Queue()
ch = 0
while(ch != 4):
    print("""Enter 1 to push element in Stack
    Enter 2 to pop element from the Stack
    Enter 3 to display element of the stack
    Enter 4 to quit """)

    ch = int(input())
    if  ch == 1:
        m = int(input("Enter the element you want to enter in the stack"))
        q.enqueue(m)
    elif ch == 2:
        q.dequeue()

    elif ch == 3:
        q.display()

    elif ch == 4:
        print("Hence we will quit")

    else:
        print("wrong choice")
