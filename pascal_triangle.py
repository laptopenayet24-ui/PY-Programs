def makerows(n):
    row=[]
    ans=1
    row.append(1)
    for i in range(n):
        ans=ans*(n-i)
        ans=ans//(i+1)
        row.append(ans)
    return row
#---------------------------------------------------------------
def pascal_triangle(n):
    ans=[]
    for i in range(n):
        ans.append(makerows(i))
    return ans
#---------------------------------------------------------------
print(pascal_triangle(5))