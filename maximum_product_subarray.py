def optimal_soln(arr,n):
    pre=1
    suff=1
    ans=float("-inf")
    for i in range(n):
        if pre==0:
            pre=1
        if suff==0:
            suff=1
        pre*=arr[i]
        suff*=arr[n-i-1]
        ans=max(ans,max(pre,suff))
    return ans
#test case---------------------------
