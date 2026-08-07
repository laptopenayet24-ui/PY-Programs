def merge(arr,low,mid,high):
    count=0
    temp=[]
    left=low
    right=mid+1
    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            count+=mid-left+1
            temp.append(arr[right])
            right+=1
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
    for i in range(len(temp)):
        arr[low+i]=temp[i]
    return count
def merge_Sort(arr,low,high):
    count=0
    if low>=high:
        return count
    mid=(low+high)//2
    count+=merge_Sort(arr,low,mid)
    count+=merge_Sort(arr,mid+1,high)
    count+=merge(arr,low,mid,high)
    return count
def count_numbers_of_inversion(arr,n):
    count=0
    count=merge_Sort(arr,0,n-1)
    return count
#test case---------------------------------------------------------------------
arr=[1,20,6,4,5]
n=len(arr)
print(count_numbers_of_inversion(arr,n))