
#Function for the selection_sort
def selection_sort(li):
    ##Traversing through each element in the list
    for i in range(0,len(li)-1):
        min_no = li[i]
        min_pos = i
        #Finding the samllest element and placing it at front
        for j in range(i,len(li)):
            if(min_no >li[j]):
                min_no = li[j]
                min_pos = j
            li[i],li[min_pos] = li[min_pos],li[i]
    #Returning the sorted list
    return li

m = int(input("number of element you want in list"))
li = []
for i in range(m):
    a= int(input())
    li.append(a)
#Calling the Selection_Sort function and printing the sorted list
print(selection_sort(li))
