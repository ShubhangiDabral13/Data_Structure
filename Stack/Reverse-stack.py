def create_stack():

    stack = []
    return stack

def push(stack,x):
    stack.append(x)

def pop(stack):
    if stack != []:
        return (stack.pop())

    else:
        return None

def display(stack):

    for i in range(len(stack)):
        print(stack[i] ,end = " ")

    print()

def insert(stack,data):

    if stack == []:
        stack.append(data)

    else:
        item = stack.pop()
        insert(stack,data)
        push(stack,item)

def reverse(stack):
    if len(stack) == 0:
        return
    temp = pop(stack)
    reverse(stack)
    insert(stack, temp)


stack = create_stack()
push(stack, 1)
push(stack, 2)
push(stack, 3)
push(stack, 4)

display(stack)

reverse(stack)

display(stack)
