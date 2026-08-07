'''if arr=[10,22,12,3,0,6] then the returning array is [22,12,6]
it is so because the elements in the returning array in the original list have no element in the right greater than them'''
def find_leaders(arr):
    int_min=float('-inf')
    rl=[]
    maxi=int_min
    length=len(arr)
    for i in range(length-1,-1,-1):
        if arr[i]>maxi:
            rl.append(arr[i])
            maxi=arr[i]
    return rl[::-1]
#=-------------------------------------------------------------------------------------
arr=[10,22,12,3,0,6]
print(find_leaders(arr))