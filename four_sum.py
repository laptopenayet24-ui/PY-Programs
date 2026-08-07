def optimal_soln(nums,target):
    n=len(nums)
    ret_lis=[]
    for i in range(n):
        if i>0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,n):
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            k=j+1
            l=n-1
            while k<l:
                sum=nums[i]+nums[j]+nums[k]+nums[l]
                if sum==target:
                    temp=[nums[i],nums[j],nums[k],nums[l]]
                    ret_lis.append(temp)
                    k+=1
                    l-=1
                    while k<l and nums[k]==nums[k-1]:
                        k+=1
                    while k<l and nums[l]==nums[l+1]:
                        l-=1
                elif sum<target:
                    k+=1
                else:
                    l-=1
    return list(set(tuple(x) for x in ret_lis))
#-----------------------------------------------------------------------------
nums=[1,0,-1,0,-2,2,2,-2,-1,1,-1,0,1,-1,0,1,-2,2]
target=0
print(optimal_soln(nums,target))