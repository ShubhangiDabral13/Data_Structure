
#Function for the insertion_sort
def insertion_sort(li):
    for i in range(1,len(li)):
        value = li[i]
        hole = i
        while(hole>0 and li[hole - 1]>value):
            li[hole] = li[hole-1]
            hole = hole-1
        li[hole] = value
    #Returning the sorted list
    return li

m = int(input("number of element you want in list"))
li = []
for i in range(m):
    a= int(input())
    li.append(a)
#Calling the insertion_sort function and printing the sorted list
print(insertion_sort(li))
