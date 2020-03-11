
"""Algorithm:
1. Declare a character stack li.
2. Now traverse the expression string exp.
  * If the current character is a starting bracket (‘(‘ or ‘{‘ or ‘[‘) then push it to stack.
  * If the current character is a closing bracket (‘)’ or ‘}’ or ‘]’) then pop from stack and if the popped character is the matching starting
  bracket then fine else parenthesis are not balanced.
3. After complete traversal, if there is some starting bracket left in stack then “not balanced” """

open_list = ["[","(","{"]
close_list = ["]",")","}"]

#Function to check for the balanced paranthesis
def check(li):
    stack = []
    for i in li:
        if i in(open_list):
            stack.append(i)
        elif i in(close_list):
            pos = close_list.index(i)
            if(len(stack) != 0 and open_list[pos] == stack[-1]):
                item = stack[-1]
                stack.remove(item)
    if(len(stack) == 0):
        return "Balanced parenthesis"
    else:
        return "Unbalanced paranthesis"

#Driver code
string = "{[]{()}}"
print(string,"-", check(string))

string = "[{}{})(]"
print(string,"-", check(string))
