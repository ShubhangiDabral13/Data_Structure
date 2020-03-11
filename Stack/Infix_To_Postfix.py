"""Algorithm
1. Scan the infix expression from left to right.
2. If the scanned character is an operand, output it.
3. Else,
…..3.1 If the precedence of the scanned operator is greater than the precedence of the operator in the stack(or the stack is empty or the stack
    contains a ‘(‘ ), push it.
…..3.2 Else, Pop all the operators from the stack which are greater than or equal to in precedence than that of the scanned operator.
    After doing that Push the scanned operator to the stack. (If you encounter parenthesis while popping then stop there and push the scanned
    operator in the stack.)
4. If the scanned character is an ‘(‘, push it to the stack.
5. If the scanned character is an ‘)’, pop the stack and and output it until a ‘(‘ is encountered, and discard both the parenthesis.
6. Repeat steps 2-6 until infix expression is scanned.
7. Print the output
8. Pop and output from the stack until it is not empty."""
#OPERATORS is a set which contain all the operators
OPERATORS = set(['+', '-', '*', '/', '(', ')'])
#PRIORITY it contain the priority of the operators
PRIORITY = {'+':1, '-':1, '*':2, '/':2}

#Function defined for the infix to postfix conversion
def infix_to_postfix(li):
    #String that will contain the postfix format off the expression
    output = ""
    stack = []
    for i in li:
        if i not in OPERATORS:
            output += i
        elif i == "(":
            stack.append("(")
        elif i == ")":
            while(stack and stack[-1]!= "("):
                a = stack[-1]
                output += a
                stack.pop()
        else:
            while(stack and stack[-1] != "(" and PRIORITY[i] <= PRIORITY[stack[-1]]):
                output  += stack.pop()
            stack.append(i)
    #For the remaing elements in stack
    while stack:
        output += stack.pop()
    print(output)

#Driver code
infix_to_postfix('1+(3+4*6+6*1)*2/3')
