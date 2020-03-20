"""
Algorithm:- To implement Stack using two Queues
1. Create a class Queue.
2. Define methods enqueue, dequeue, is_empty and get_size inside the class Queue.
3. Create a class Stack with instance variable q initialized to an empty queue.
4. Pushing is done by enqueuing data to the queue1.
5.When poping out element is done by dequeuing  all the element from queue1(expect last) and pushing them through the enqueue operation on queue2
after that removing the last element from the queue1 and then swapping the name of queue1 and queue2.
"""
class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return (self.queue == [])

    def enqueue(self,a):
        self.size += 1
        self.queue.append(a)

    def dequeue(self):
        self.size -= 1
        return(self.queue.pop(0))

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self,a):
        self.q1.enqueue(a)

    def pop(self):
        for i in range(self.q1.get_size()-1):
            a = self.q1.dequeue()
            self.q2.enqueue(a)
        m = self.q1.dequeue()
        self.q1,self.q2 = self.q2,self.q1

        print("The element that has been deleted is {}".format(m))

    def display(self):
        for i in range(self.q1.get_size()):
            print(self.q1.queue[i],end = " ")

s = Stack()
ch = 0
while(ch != 4):
    print("""Enter 1 to push element in Stack
    Enter 2 to pop element from the Stack
    Enter 3 to display element of the stack
    Enter 4 to quit """)

    ch = int(input())
    if  ch == 1:
        m = int(input("Enter the element you want to enter in the stack"))
        s.push(m)
    elif ch == 2:
        s.pop()

    elif ch == 3:
        s.display()

    elif ch == 4:
        print("Hence we will quit")

    else:
        print("wrong choice")
