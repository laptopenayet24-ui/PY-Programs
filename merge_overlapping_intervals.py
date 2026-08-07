def optimal_soln(arr):
    n=len(arr)
    ans=[]
    for i in range(n):
        if len(ans)==0 or arr[i][0]>ans[-1][1]:
            ans.append(arr[i])
        else:
            ans[-1][1]=max(ans[-1][1],arr[i][1])
    return ans
#-----------------------------------------------------------------------------
arr=[[1,3],[2,4],[5,7],[6,8],[9,10]]
print(optimal_soln(arr))