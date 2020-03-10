#defining the max_heapify function
def max_heapify(a,n,i):
    #Largest value
    largest = i
    #Left child
    l = 2*i + 1
    #Right child
    r = 2*i + 2
    #If left child exist then check the condition
    if (l < n and a[l] > a[largest]):
        largest =  l
    #If right child exist then check the condition
    if (r < n and a[r] > a[largest]):
        largest = r
    #root
    if largest != i:
        #To swap the value
        a[i],a[largest] = a[largest],a[i]
        #recursively calling the max_heapify function
        max_heapify(a,n,largest)

#Defining the built_max_heap
def built_max_heap(a):
    n = len(a)
    for i in range(n//2 , -1,-1):
        max_heapify(a,n,i)

a = [23,12,97,24,11,10]
#Calling the function
built_max_heap(a)
n = len(a)
for i in range(n):
   print (a[i],end=" ")
