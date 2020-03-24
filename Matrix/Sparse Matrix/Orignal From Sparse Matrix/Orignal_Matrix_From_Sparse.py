#Function to convert sparse matrix into orignal matrix
def orignal_mat(sparse_mat):
    row = sparse_mat[0][0]
    column = sparse_mat[0][1]
    #Initializing original matrix.
    orig_mat = [[0 for i in range(column)]for j in range(row)]

    #filling the orignal matrix with non zero terms from sparse matrix
    for i in range(1,len(sparse_mat)):
        orig_mat[sparse_mat[i][0]][sparse_mat[i][1]] = sparse_mat[i][2]

    #Displaying orignal matrix
    for i in orig_mat:
        print(i)
#Main function
sparse_mat =[[5 ,6, 6],
            [0, 4, 9],
            [1, 1, 8],
            [2, 0, 4],
            [2, 3, 2],
            [3, 5, 5],
            [4, 2, 2]]
orignal_mat(sparse_mat)
