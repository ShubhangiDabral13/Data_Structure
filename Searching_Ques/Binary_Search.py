def binary_search(li,n,max_pos,min_pos):
    while max_pos >= min_pos:
        mid = (max_pos+min_pos)//2
        if (n >li[mid]):
            min_pos = mid+1
        elif(n<li[mid]):
            max_pos = mid -1
        elif (n == li[mid]):
            return (" {} found in list at position {}".format(n , mid+1))
    return ("element not foundz")

m = int(input("enter the number of element in list"))
li = []
for i in range(m):
    a = int(input())
    li.append(a)
li.sort()
n = int(input("enter the number you want to search"))
max_pos,min_pos = m-1 , 0
print(binary_search(li,n,max_pos,min_pos))
