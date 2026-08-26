def possible(arr,day,m,k):
    n=len(arr)
    count=0
    noBoq=0
    for i in range(n):
        if arr[i]<=day:
            count+=1
        else:
            noBoq+=count//k
            count=0
    noBoq+=count//k
    if noBoq>=m:
        return True
    return False
def optimal_soln(arr,m,k):
    if len(arr)<m*k:
        return -1
    low,high=min(arr),max(arr)
    while low<=high:
        mid=(low+high)//2
        if possible(arr,mid,m,k):
            high=mid-1
        else:
            low=mid+1
    return low