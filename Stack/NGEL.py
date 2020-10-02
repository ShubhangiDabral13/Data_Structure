
# Problem: Given an array, print the Next Greater Element (NGE) for every element.
# 		 The Next Greater Element for an element x is the first greater element
# 		 on the left side of x in array. Elements for which no greater element exist,
# 		 consider next greater element as -1.


def next_greater_element_left(arr):
    s = []
    v = []

    for i in range(0,len(arr)):
        while(len(s)!= 0 and s[-1]<arr[i]):
            s.pop()

        if len(s) == 0:
            v.append(-1)

        else:
            v.append(s[-1])

        s.append(arr[i])

    return v


if __name__ == '__main__':

	arr = [7, 8, 1, 4]
	ans = next_greater_element_left(arr)
	print(ans)

"""
Output:
[-1,-1,8,8]
"""
