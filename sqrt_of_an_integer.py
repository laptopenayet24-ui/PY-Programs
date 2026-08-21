def optimal_soln(n):
    low,high=0,n
    while low<=high:
        mid=(low+high)//2
        if mid**2<=n:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans
#------------TEST CASES_________