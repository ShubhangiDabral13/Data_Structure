def print_pattern(num,m,flag):
    print(m)
    if flag == False and num == m:
        return
    if flag:
        if m-5>0:
            print_pattern(num,m-5,True)
        else:
            print_pattern(num,m+5,False)
    else:
        print_pattern(num,m+5,False)
n = int(input("Enter the number whose pattern you want to find out"))
print_pattern(n,n,True)
