
#Class containing th function to perform the basic function by Double_ended_queue
class Double_ended_queue:
    #Ton initialize th parameters
    def __init__(self,dequeue,maxsize):
        self.dequeue = dequeue
        self.maxsize = maxsize
        self.front = -1
        self.rear = -1

    #To add the element from the rear end ofe dequeue
    def insert_from_rear(self):
        #Condition to check for overflow of double ended Queue
        if((self.front == 0 and self.rear == maxsize -1) or(self.front == self.rear+1)):
            print("double ended queue overflow")
        elif self.front == -1 and self.rear ==-1:
            self.front = 0
            self.rear = 0
        elif self.rear == self.maxsize -1:
            self.rear == 0
        else:
            self.rear += 1
        #Asking the user to enter the element that user want to insert in dequeue
        a = int(input("Enter the element you want to insert"))
        dequeue[self.rear]  = a

    #To add the element from the front end of dequeue
    def insert_from_front(self):
        #Condition to check for the overflow of double ended queue
        if((self.front == 0 and self.rear == maxsize-1) or(self.front == self.rear+1)):
            print("double_ended queue overflow")
        elif self.front == -1 and self.rear == -1:
            self.rear == 0
            self.front == 0
        elif self.front == 0:
            self.front += self.maxsize -1
        else:
            self.front  -= 1
        #Asking the user to enter the element that user want to insert indequeue
        a = int(input("Enter the element you want to enter"))
        dequeue[self.front]  = a

    #To delete the element from the front end of dequeue
    def delete_from_front(self):
        #Condition to check for the underflow of double ended queue
        if (self.front == -1 and self.rear == -1 ):
            print("double_ended queue underflow")
        else:
            a = dequeue[self.front]
            if self.front == self.rear:
                self.front ,self.rear = -1,-1
            elif self.front == maxsize-1:
                self.front = 0
            else:
                self.front += 1
        #The element  which is deleted is being displayed
        print("The element which is deleted from front end is {}".format(a))


    #To delete the element from the rear end of dequeue
    def delete_from_rear(self):
        #Condition to check for the underflow of double ended queue
        if(self.front == -1 and self.rear == -1):
            print("double_ended queue underflow")
        else:
            a = dequeue[self.rear]
            if self.rear == self.front:
                self.rear,self.front = -1,-1
            elif self.rear == 0:
                self.rear = maxsize -1
            else:
                self.rear -= 1
        #The element which is deleted is being displayed
        print("The element which is deleted from rear is {}".format(a))


    def display(self):
        #Check the condition for the underflow
        if(self.front == -1 and self.rear == -1):
            print("Double_ended_queue underflow")

        if (self.front> self.rear):
            for i in range(self.front,maxsize):
                print(dequeue[i],end = " ")
            for j in range(self.rear+1):
                print(dequeue[j],end = " ")
        else:
            for i in range(self.front,self.rear+1):
                print(dequeue[i],end = " ")

#Main
#maximum size of the  dequeue user want
maxsize = int(input("Enter the maximum size of the queue\n"))
#initializing the dequeue
dequeue = [0]*maxsize
obj = Double_ended_queue(dequeue,maxsize)
choice =0
while choice != 6:
        print("""enter 1 to push a value from rear
        enter 2 to push a value from front
        enter 3 to pop the element from front
        enter 4 to pop the element from rear
        enter 5 to display the element of dequeue queue
        enter 6 to quit """)

        choice  = int(input())
        if choice == 1:
            obj.insert_from_rear()

        elif choice == 2:
            obj.insert_from_front()

        elif choice == 3:
            obj.delete_from_front()

        elif choice == 4:
            obj.delete_from_rear()

        elif choice == 5:
            print("The elements are")
            obj.display()

        elif choice == 6:
            print("want to quit")

        else:
            print("Wrongchoice")
