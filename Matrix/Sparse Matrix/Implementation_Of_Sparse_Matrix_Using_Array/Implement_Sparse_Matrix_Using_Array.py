"""
2D array is used to represent a sparse matrix in which there are three rows named as

Row: Index of row, where non-zero element is located
Column: Index of column, where non-zero element is located
Value: Value of the non zero element located at index – (row,column)
"""

def sparse_matrix(arr):
    rows,column = len(arr),len(arr[0])
    count = 0
    for i in range(rows):
        for j in range(column):
            if arr[i][j] != 0 :
                count += 1

    sparse_mat = [[0]*3]*(count+1)
    
    sparse_mat[0] = [rows,column,count]
    k = 1
    for i in range(rows):
        for j in range(column):
            if arr[i][j] != 0:
                sparse_mat[k] = [i,j,arr[i][j]]
                k =k+1


    for i in sparse_mat:
        print(i)
sparse_matrix([[0,0,3,0,4],[0,0,5,7,0],[0,0,0,0,0],[0,2,6,0,0]])
