def binarySearch(arr,low,high,target):
    if low>high:
        return -1
    mid=(high+low)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return binarySearch(arr,mid+1,high,target)
    else:
        return binarySearch(arr,low,mid-1,target)
#------------------------------------------