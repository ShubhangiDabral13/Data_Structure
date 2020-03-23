def sparse_matrix(arr):
    rows,column = len(arr),len(arr[0])
    count = 0
    for i in range(rows):
        for j in range(column):
            if arr[i][j] != 0 :
                count += 1

    row1,column1 = (3,count)
    new_arr = [[0 for i in range(row1)] for j in range(column1)]

    k = 0

    for i in range(rows):
        for j in range(column):
            if arr[i][j] != 0:
                new_arr[k][0] = j
                new_arr[k][1] = i
                new_arr[k][2] = arr[i][j]
                k += 1


    for i in new_arr:
        print(i)
sparse_matrix([[0,0,3,0,4],[0,0,5,7,0],[0,0,0,0,0],[0,2,6,0,0]])
