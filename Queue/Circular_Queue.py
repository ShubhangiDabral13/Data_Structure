
#class to implement the basic function on circular queue
class Circular_Queue:
    #Constructor to initialize the variable
    def __init__(self,cqueue,maxsize):
        self.cqueue = cqueue
        self.maxsize = maxsize
        self.rear = -1
        self.front  = -1

    #To add the element to the Queue
    def insert_element(self):
        #To check for the overflow of the cicular Queue
        if((self.rear == maxsize -1 and self.front == 0 ) or(self.front == self.rear+1)):
            print("Circular_Queue overflow")
        #If both rear and front are -1 assign value zero to them
        elif self.rear == -1 and self.front == -1:
            self.rear = 0
            self.front = 0
        #If rear reaches the end of the circular queue ,assign zero to it
        elif self.rear == self.maxsize -1:
            self.rear  = 0
        else:
            self.rear += 1
        a = int(input("Enter the element you want to enter in queue\n"))
        cqueue[self.rear] = a

    #To delete the element from the Circular queue
    def delete_element(self):
        #To check for underflow condition
        if(self.front == -1 and self.rear == -1):
            print("Circular_Queue underflow")
        else:
            a = cqueue[self.front]
            #in this case there is no element in Circular qeueue so initialize both to -1
            if self.front == self.rear:
                self.front,self.rear = -1,-1
            #If front is at the end circular queue assign zero to it.
            elif self.front == maxsize - 1:
                self.front = 0
            else:
                print(self.front)
                self.front += 1
            print(self.front)

            print("The element which has been deleted is {}".format(a))

   #To display element of the circular queue
    def display(self):
        #Check the condition for the underflow
        if(self.front == -1 and self.rear == -1):
            print("Circular_Queue underflow")

        if (self.front> self.rear):
            for i in range(self.front,maxsize):
                print(cqueue[i],end = " ")
            for j in range(self.rear+1):
                print(cqueue[j],end = " ")
        else:
            for i in range(self.front,self.rear+1):
                print(cqueue[i],end = " ")


#main function
#maximum size of the circular queue user want
maxsize = int(input("Enter the maximum size of the queue\n"))
#initializing the cqueue
cqueue = [0]*maxsize
obj = Circular_Queue(cqueue,maxsize)
choice =0
while choice != 4:
        print("""enter 1 to push a value
        enter 2 to pop a value
        enter 3 to display the element in  circular queue
        enter 4 to quit """)

        choice  = int(input())
        if choice == 1:
            obj.insert_element()

        elif choice == 2:
            obj.delete_element()

        elif choice == 3:
            obj.display()

        elif choice == 4:
            print("quit from the program")

        else:
            print("Wrongchoice")
