
"""ALOGORITHM TO CALCULATE/EVALUATE POSTFIX EXPRESSION:-
1) Create a stack to store operands (or values).
2) Scan the given expression and do following for every scanned element.
…..a) If the element is a number, push it into the stack
…..b) If the element is a operator, pop operands for the operator from stack. Evaluate the operator and push the result back to the stack
3) When the expression is ended, the number in the stack is the final answer"""

#Function to calculate postfix expression
def evaluate(exp):
    #stack where oprands are pushed
    stack = []
    ans =0
    #traversing through the expression
    for i in exp:
        #if the value is the digit then we will append it to the stack
        if i.isdigit():
            stack.append(i)
        else:
            #pop two value from stack and evalute the operator and push the result back to stack
            value1 = stack[-1]
            stack.pop()
            value2 = stack[-1]
            stack.pop()
            ans = str(eval(value2+i+value1))
            stack.append(ans)
    stack = [int(j) for j in stack]
    return stack

#Driver function
exp = "231*+9-"
print(evaluate(exp))
