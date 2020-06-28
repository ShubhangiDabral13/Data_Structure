def findmedian(arr,k):
    left = 0
    right = left + (k -1)
    result = []


    while(right  < len(arr)):
        new_list = arr[left:right+1]
        new_list.sort()


        if k % 2 == 0:
            mid_point = (k)//2
            median = (new_list[mid_point] + new_list[mid_point - 1])/2

        else:

            median = new_list[(k)//2]


        result.append(median)
        left += 1
        right += 1

    return result


arr =  [1, 5, 13, 8, 2, 3, 3, 1]
k = 3
print(findmedian(arr,k))

"""
Output:
[6, 6, 5, 3, 2]
"""

arr =  [1, 5, 13, 8, 2, 3, 3, 1]
k = 3
print(findmedian(arr,k))

"""
Output:
[6.5, 6.5, 5.5, 3.0, 2.5]
"""
