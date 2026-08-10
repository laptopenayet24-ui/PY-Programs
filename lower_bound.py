def lowerBoound(arr,x):
    n=len(arr)
    low=0
    high=n-1
    ans=n
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=x:
            ans=mid
            #look into more smaller index
            high=mid-1
        else:
            low=mid+1
    return ans