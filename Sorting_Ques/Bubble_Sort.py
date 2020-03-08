
#Function for bubble sort
def bubble_sort(li):
    #Traversing through each element in the list
    for i in range(0,len(li)-1):
        for j in range(0,len(li)-i-1):
            if(li[j]>li[j+1]):
                #If next element is greater than the current element we will swap it
                li[j],li[j+1] = li[j+1],li[j]
    #Returning the sorted list
    return li

m = int(input("number of element you want in list"))
li = []
for i in range(m):
    a= int(input())
    li.append(a)
#Calling the bubble_sort function and printing the sorted list    
print(bubble_sort(li))
