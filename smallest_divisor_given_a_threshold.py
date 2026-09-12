from math import ceil

def optimal_soln(arr,threshold):
    if threshold<len(arr):
        return -1
    low,high=1,max(arr)
    ans=-1
    while low<=high:
        mid=(high+low)//2
        sum=0
        n=len(arr)
        for i in range(0,n):
            sum+=ceil(arr[i]/mid)
        if sum<=threshold:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
#--------------------------TEST CASES----------------------------