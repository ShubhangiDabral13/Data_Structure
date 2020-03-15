"""
ALGORITHM TO CONVERT POSTFIX TO INFIX
1.While there are input symbol left
…1.1 Read the next symbol from the input.
2.If the symbol is an operand
…2.1 Push it onto the stack.
3.Otherwise,
…3.1 the symbol is an operator.
…3.2 Pop the top 2 values from the stack.
…3.3 Put the operator, with the values as arguments and form a string.
…3.4 Push the resulted string back to stack.
4.If there is only one value in the stack
…4.1 That value in the stack is the desired infix string.
"""

#to check whether the particular value is oprand or not
def isoprand(x):
    return ((x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z'))

#To convert the expression from postfix to infix
def converts(exp):
    #empty stack to store the result
    stack = []
    #traversing through the expression
    for i in exp:
        #To check if particular value is digit or not
        if  i.isdigit():
            stack.append(i)
        #To check if particular value is operand or not
        elif (isoprand(i)):
            stack.append(i)
        else:
            value1 = stack[-1]
            stack.pop()
            value2 = stack[-1]
            stack.pop()
            stack.append("("+value2+i+value1+")")
    #eturning the top most value from the stack because stack contain only one element.        
    return stack.pop()

# driver Function
exp = "23*5+"
print(converts(exp))

exp = "ab*c+d*e/"
print(converts(exp))
