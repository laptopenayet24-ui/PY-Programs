def optimal_soln(m,n):
    low,high=0,m
    while low<=high:
        mid=(high+low)//2
        if mid**n==m:
            return mid
        elif mid**n<m:
            low=mid+1
        else:
            high=mid-1
    return -1
#-------------------TEST CASES-------------------
print(optimal_soln(27,3)) # 3