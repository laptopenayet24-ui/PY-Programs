def optimal_soln(arr,cows):
    n=len(arr)
    arr.sort()
    low,high=0,arr[n-1]-arr[0]
    while low<=high:
        mid=(low+high)//2
        if canplaceCows(arr,mid,cows):
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return high

def canplaceCows(arr,mid,cows):
    lastpos=arr[0]
    count=1
    for i in range(1,len(arr)):
        if arr[i]-lastpos>=mid:
                lastpos=arr[i]
                count+=1
        if count>=cows:
            return True
    return False
#----------------------------------------------------------
#test cases
arr=[1,2,8,4,9]
cows=3
print(optimal_soln(arr,cows))