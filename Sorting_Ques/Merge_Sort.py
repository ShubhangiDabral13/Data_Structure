
#Creating the function for merge_sort
def merge_sort(a):
    # we will split the the list to left and right if there is more than one element in it.
    if(len(a)>1):
        mid = len(a)//2
        #left half contain element from starting till one less than the middle element
        left = a[:mid]
        #Right half contain element from middle till the end.
        right = a[mid:]
        #recursive calling the merge_sort Function
        merge_sort(left)
        merge_sort(right)
        #Counter i for left list indexing
        #Counter j for right list indexing
        #counter k for the main list indexing that need to be sorted
        i,j,k = 0 ,0, 0
        while(i<len(left) and j<len(right)):
            #Left element is smaller than the right element we will add it to the main list
            if(left[i] < right[i]):
                a[k] = left[i]
                k += 1
                i += 1
            else:
                #else if right element isn smaller or equal to the left element we will add it to the main list
                a[k] = right[j]
                k += 1
                j += 1
        while i<len(left):
            #Adding all the remaing element from right list to the main nlist
            a[k] = left[i]
            k += 1
            i += 1
        while j<len(right):
            #Adding all the remaing element from right list to the main list
            a[k] = right[j]
            k += 1
            j +=1
nlist = [14,46,43,27,57,41,45,21,70]
#calling the merge_sort function and passssing the list to it.
merge_sort(nlist)
#printing the sorted list.
print(nlist)
