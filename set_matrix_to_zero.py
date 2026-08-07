''' see in the copy'''
#--------------------------------------------------------------------------------------------
def better_soln(mat,n,m):
    arr_row=[0]*n
    arr_col=[0]*m
    for i in range(n):
        for j in range(m):
            if mat[i][j]==0:
                arr_row[i]=1
                arr_col[j]=1
    for i in range(n):
        for j in range(m):
            if arr_row[i]==1 or arr_col[j]==1:
                mat[i][j]=0
#--------------------------------------------------------------------------
def better_soln(mat):
    pa




















#---------------------------------------------------------------------------
mat=[[1,1,1,1],
     [1,0,0,1],
     [1,1,0,1],
     [1,1,1,1]]
n=len(mat)
m=len(mat[0])
better_soln(mat,n,m)
print(mat)