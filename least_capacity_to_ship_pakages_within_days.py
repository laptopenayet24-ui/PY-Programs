def optimal_soln(arr,days):
    def day(arr,cap):
        day=1
        load=0
        for i in range(len(arr)):
            if load+arr[i]>cap:
                day=day+1
                load=arr[i]
            else:
                load+=arr[i]
        return day
    #-------------------------------------------------
    low=max(arr)
    high=sum(arr)
    while low<=high:
        mid=(low+high)//2
        reqDays=day(arr,mid)
        if reqDays<=days:
            high=mid-1
        else:
            low=mid+1
    return low
#---------------------------------------