# Problem: Given an array, find an array of Next Greater Elements (NGE) for every element.
# 		 The Next Greater Element for an element x is the first greater element
# 		 on the right side of x in array. Elements for which no greater element exist,
# 		 consider next greater element as -1.


def next_greater_element_right(arr):
    s = []
    v = []

    for i in range(len(arr)-1,-1,-1):
        while(len(s)!= 0 and s[-1]<arr[i]):
            s.pop()

        if len(s) == 0:
            v.append(-1)

        else:
            v.append(s[-1])

        s.append(arr[i])

    v.reverse()
    return v

if __name__ == '__main__':

	arr = [7, 8, 1, 4]
	ans = next_greater_element_right(arr)
	print(ans)


"""
Output:
[8,-1,4,-1]
"""
