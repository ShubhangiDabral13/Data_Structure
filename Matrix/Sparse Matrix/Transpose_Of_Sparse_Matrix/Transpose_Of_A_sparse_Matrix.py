def sparse_matrix(arr):
    rows,column = len(arr),len(arr[0])
    count = 0
    for i in range(rows):
        for j in range(column):
            if arr[i][j] != 0 :
                count += 1

    sparse_mat = [[0]*3]*(1+count)
    sparse_mat[0] = [column,rows,count]

    k = 1

    for i in range(rows):
        for j in range(column):
            if arr[i][j] != 0:
                sparse_mat[k] =[j,i,arr[i][j]]
                k += 1

    for i in sparse_mat:
        print(i)

sparse_matrix([[0,0,3,0,4],[0,0,5,7,0],[0,0,0,0,0],[0,2,6,0,0]])
