class stack:

    def __init__(self,stack1,max1):
        self.stack1 = stack1
        self.max1 = max1

    def push(self):
        if(len(stack1) == max1):
            print("the stack is full ..overflow of stack\n")
        else:
            a = int(input("enter the number u want to add to stack\n"))
            stack1.append(a)

    def pop(self):
        if(len(stack1) == 0):
            print("stack is underflow")

        else:
            a = stack1[-1]
            stack1.remove(a)
            print("the item that has been poped out is{}\n".format(a))

    def peep(self):
        a = stack1[-1]
        print("element at the top of stack right now {}\n".format(a))



    def display(self):
        l=len(stack1)
        print("the element in stack are \n")
        for i in range(l):
            print(stack1[i])

max1=int(input("the maximum length of the stack you want\n"))
stack1=[]
obj=stack(stack1,max1)
choice=0
while choice!=5:

    print("""enter 1 to push a value
            enter 2 to pop a value
            enter 3 to peep top value
            enter 4 to dislay the stack
            enter 5 to quit """)

    choice = int(input())
    if choice == 1:
        obj.push()

    elif choice == 2:
        obj.pop()

    elif choice == 3:
        obj.peep()

    elif choice == 4:
        obj.display()

    else:
        print("wrong entry")
