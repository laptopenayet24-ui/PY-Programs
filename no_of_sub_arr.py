#no of subarrays with sum =k
def optimal(arr,k):
    l=len(arr)
    hash_map={0:1}
    presum=0
    count=0
    for i in range(l):
        presum+=arr[i]
        rmv=presum-k
        count+=hash_map.get(rmv, 0)
        hash_map[presum] = hash_map.get(presum, 0) + 1
    return count
#-----------------------------------------------------------------
arr=[1, 1, 1]
k=2
print(optimal(arr,k))