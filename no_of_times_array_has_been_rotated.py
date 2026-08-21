def optimal_soln(arr):
    ans=float("inf")
    n=len(arr)
    low,high=0,n-1
    while low<=high:
        mid=(low+high)//2
        if arr[low]<=arr[high]:
            ans=min(ans,arr[low])
            break
        if arr[low]<=arr[mid]:
            ans=min(ans,arr[low])
            low=mid+1
        else:
            high=mid-1
            ans=min(ans,arr[mid])
    return ans
#------TEST CASES----------------

