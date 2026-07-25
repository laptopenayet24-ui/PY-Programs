'''arr=[2,1,5,4,3,0,0] then output should be [2,3,0,0,1,4,5]'''
def nxtperm(arr):
    #finding the dip
    l=len(arr)
    ind=False
    for i in range(l-2,-1,-1):
        if (arr[i]<arr[i+1]):
            ind=i
            break
    for i in range(l-1,ind,-1):
        if arr[i]>arr[ind]:
            arr[ind],arr[i]=arr[i],arr[ind]
            break
    arr=arr[0:ind+1]+arr[ind+1:][::-1]
    return arr
#--------------------------------------------------------------------------------
arr=[2,1,5,4,3,0,0]
print(nxtperm(arr))