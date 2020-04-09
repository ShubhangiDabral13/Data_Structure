def check(num,num1):
    if num == 0:
        return(num1)
    num1 = num1*10 + int(num%10)
    return(check(num//10,num1))


# Driver Function
num = int(input("Enter the number of your choice"))
num1 = 0
ans = check(num,num1)
if(ans == num):
    print("YES")
else:
    print("No")
