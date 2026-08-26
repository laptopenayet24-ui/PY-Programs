from math import ceil


def findHours(hr,arr):
    totalH=0
    n=len(arr)
    for i in range(n):
        totalH+=ceil(arr[i]/hr)
    return totalH
def optimal_soln(arr,k):
    low=1
    high=max(arr)
    ans=float('inf')
    while low<=high:
        mid=(low+high)//2
        totalH=findHours(mid,arr)
        if totalH<=k:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
#-----------------TEST CASES-----------------------