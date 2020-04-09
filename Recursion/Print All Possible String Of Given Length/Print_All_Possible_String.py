def print_all(charset,str,k,n):
    if k == 0:
        print(str)
        return
    for i in range(n):
        new_str = str + charset[i]
        print_all(charset,new_str,k-1,n)


charset = ["a","b","c"]
k = 3
n = len(charset)
print_all(charset," ",k,n)
