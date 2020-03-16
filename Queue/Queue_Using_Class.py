
#Class Queue which contain all the function to perform the basic operation on queue
class Queue:
    #Constructor to initialize various parameters
    def __init__(self,queue,maxsize):
        self.queue = queue
        self.maxsize = maxsize
        self.rear = -1
        self.front = -1
    #function to add an element to the queue
    def enqueue(self):
        #Check for the queue overflow
        if self.rear == (maxsize-1):
            print("queue overflow")
        else:
            #asking which element user want to add to the queue
            a = int(input("Enter the element you want to insert in stack"))
            if self.rear == -1:
                self.front += 1
            queue.append(a)
            self.rear += 1

    #Function to remove element from the Queue
    def dequeue(self):
        #Check for the queue underflow
        if self.front == -1 or self.front>self.rear:
            print("queue underflow")
        else:
            a = queue[-1]
            queue.remove(a)
            print("The element that is poped out is {}".format(a))
            self.front =+ 1

    #To display the top most element in queue
    def peep(self):
        #Checking for the queue underflow
        if self.front == -1 or self.front> self.rear:
            print("queue underflow")
        else:
            a = queue[-1]
            print("The top most element at queue is {}".format(a))

    #Function to dislay all the element form the Queue
    def display(self):
        print("The element in queue are:-")
        for i in range(len(queue)):
            print(queue[i],end = " ")


#main Function
queue =[]
maxsize = int(input("Enter the maximum size of the queue\n"))
obj = Queue(queue,maxsize)
choice =0
while choice != 5:
        print("""enter 1 to push a value
        enter 2 to pop a value
        enter 3 to peep top value
        enter 4 to dislay the stack
        enter 5 to quit """)

        choice  = int(input())
        if choice == 1:
            obj.enqueue()

        elif choice == 2:
            obj.dequeue()

        elif choice == 3:
            obj.peek()

        elif choice == 4:
            obj.display()

        else:
            print("Wrongchoice")
