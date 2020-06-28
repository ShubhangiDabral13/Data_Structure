def find_sum(arr,k):

    if len(arr) < k:
        print("Invalid")
        return


    sum_window = sum(arr[:k])
    max_sum = sum_window
    for i in range(len(arr)-k):
        sum_window = sum_window - arr[i] + arr[i+k]
        max_sum = max(max_sum,sum_window)

    print("The maximum in arr is {}".format(max_sum))


# Driver code
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
find_sum(arr, k)

"""
output:
The maximum sum in array is 24

"""
