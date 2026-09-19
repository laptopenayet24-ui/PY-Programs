def optimal_soln(arr,k):
    n=len(arr)
    low,high=0,n-1
    while low<=high:
        mid=low+(high-low)//2
        missing=arr[mid]-(mid+1)
        if missing<k:
            low=mid+1
        else:
            high=mid-1
    return low+k
#test cases
arr=[2,3,4,7,11]
k=5
print(optimal_soln(arr,k))