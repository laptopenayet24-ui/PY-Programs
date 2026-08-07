def optimal_solution(nums,k):
    hash_map={0:1}
    count=0
    xr=0
    n=len(nums)
    for i in range(n):
        xr=xr^nums[i]
        x=xr^k
        if x in hash_map:
            count+=hash_map[x]
        hash_map[xr]=hash_map.get(xr, 0) + 1
    return count
#-----------------------------------------------------------------------------
nums=[4,2,2,6,4]    
k=6
print(optimal_solution(nums,k))