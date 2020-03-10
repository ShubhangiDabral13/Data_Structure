#Stack implementation using  list
#Push is used to insert new element in the list
def push():
    #condition to check for the Overflow
    if(len(li) == max_len):
        print("Overflow")
    else:
        n =int(input("enter the number you want to enter"))
        li.append(n)


#Pop is used to remove the last element from the list
def pop():
    #condition to check  for underflow
    if(len(li) == 0):
        print("underflow")
    else:
        top -= 1
        item = li[-1]
        li.remove(item)

#To display the top most element from the list
def peek():
    #condition to check for Overflow
    if(len(li) == 0):
        print("underflow")
    else:
        print("The top most element is {}".format(li[-1]))

#To display all the element from the list
def show():
    print("the element in the list are")
    for i in range(len(li)):
        print(li[i],end =" ")


#main function
#Maximum lenght of the list
max_len = int(input("enter the maximum length of the list"))
li = []
ch = 0
while(ch != 5):
    print("""Enter 1 to push element.
Enter 2 to pop element.
Enter 3 to display top most element.
Enter 4 to display all element in list.
Enter 5 to quit.
Enter Your choice""")
    ch = int(input())
    if ch == 1:
        push()
    elif ch == 2:
        pop()
    elif ch == 3:
        peek()
    elif ch == 4:
        show()
    else:
        print("Wrong choice")
