
#Creating a function quick_sort
def quick_sort(a,start,end):
    #Base condition for the recursion
    if start< end:
        pindex = partition(a,start,end)
        #recursively calling quick_sort
        quick_sort(a,start,pindex-1)
        quick_sort(a,pindex+1,end)
#Creating the partition function which will return the index for the pivot  whose right side contain element greater than pivot and left side smaller than pivot.
def partition(a,start,end):
    pivot = a[end]
    pindex = start
    for i in range(start,end):
        if(a[i] <= pivot):
            a[i],a[pindex] = a[pindex],a[i]
            pindex += 1

    a[pindex],a[end] = a[end],a[pindex]
    return pindex

m = int(input("Enter the number of element you want to enter"))
li = []
for i in range(m):
    a = int(input())
    li.append(a)
#calling that function.
quick_sort(li,0,m-1)
#Printing the sorted list.
print(li)
