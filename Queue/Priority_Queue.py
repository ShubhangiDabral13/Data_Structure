"""
Priority Queue is an extension of the queue with following properties.
1) An element with high priority is dequeued before an element with low priority.
2) If two elements have the same priority, they are served according to their order in the queue.
"""

class Priority_Queue:
    def __init__(self):
        self.pqueue = []
        self.size = 0

    def enqueue(self,a):
        self.size += 1
        self.pqueue.append(a)

    def dequeue(self):
        max= 0
        if self.size == 0:
            print("Priority_Queue is empty")
        for i in range(self.size):
            if(self.pqueue[i]>self.pqueue[max]):
                max = i
        a = self.pqueue.pop(max)
        self.size -= 1
        print("The deleted element is {}".format(a))

    def display(self):
        if self.size == 0:
            print("Priority_Queue is empty")
        print("element in Priority_Queue are:-")
        for i in range(self.size):
            print(self.pqueue[i],end = " ")

pq = Priority_Queue()
ch = 0
while(ch != 4):
    print("""\nEnter 1 to add element to the Priority_Queue
    Enter 2 to delete element from the Priority_Queue
    Enter 3 to display element of the Priority_Queue
    Enter 4 to quit """)

    ch = int(input())
    if  ch == 1:
        m = int(input("Enter the element you want to enter in the stack"))
        pq.enqueue(m)
    elif ch == 2:
        pq.dequeue()

    elif ch == 3:
        pq.display()

    elif ch == 4:
        print("Hence we will quit")

    else:
        print("wrong choice")
