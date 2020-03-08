# Linear Search function in which 2 variables are passed.Li which contain the list of numbers. and n the number we want to search.
def linear_seatch(li,n):
    for i in range(len(li)):
        if li[i] == n:
            print(li[i])
            return("element found out at position {}".format(i))

    else:
        return("Element not present")

m = int(input("enter the number of element you want to enter in list"))
li =[]
for i  in range(m):
    a= int(input())
    li.append(a)

n = int(input("Enter the number you want to search"))
print(linear_seatch(li,n))
