"""
Algorithm:- To implement stack using one queue.
1. Create a class Queue.
2. Define methods enqueue, dequeue, is_empty and get_size inside the class Queue.
3. Create a class Stack with instance variable q initialized to an empty queue.
4. Pushing is done by enqueuing data to the queue.
5. To pop, the queue is dequeued and enqueued with the dequeued element n – 1 times where n is the size of the queue.
 This causes the the last element added to the queue to reach the rear of the queue. The queue is dequeued one more time to get the item to be
 returned.
6. The method is_empty returns True iff the queue is empty.

"""

class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def is_empty(self):
        return(self.queue == [])

    def enqueue(self,a):
        self.size += 1
        self.queue.append(a)

    def dequeue(self):
        self.size -= 1
        return(self.queue.pop())

    def get_size(self):
        return self.size

class Stack:
    def __init__(self):
        self.q = Queue()

    def is_empty(self):
        return self.q.is_empty()

    def push(self,a):
        self.q.enqueue(a)

    def pop(self):
        for j in range(self.q.get_size()-1):
            a = self.q.dequeue()
            self.q.enqueue(a)
        p = self.q.dequeue()
        print("The element which is being deleted is {}".format(p))

    def display(self):
        for i in range(self.q.get_size()):
            print(self.q.queue[i],end = " ")


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
