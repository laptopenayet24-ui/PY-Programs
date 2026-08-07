'''rotate matrix'''
def optimal_soln(mat):
    n=len(mat)
    #transpose
    for i in range(0,n-1):
        for j in range(i+1,n):
            mat[i][j]=mat[j][i]
    #reverse rows
    for i in range(n):
        mat[i]=mat[i][::-1]
#=---------------------------------------------------------------------
mat=[[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]
optimal_soln(mat)
print(mat)