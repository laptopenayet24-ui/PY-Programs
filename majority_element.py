'''def better_soln(arr):
    hash_map={}
    for i  in arr:
        if i in hash_map:
            hash_map[i]+=1
        else:
            hash_map[i]=1
    keys=list(hash_map.keys())
    values=list(hash_map.values())
    el=keys[values.index(max(values))]
    return el
arr=[1,1,3,3,3,3,3,3,5,6,7,8,9,0]
print(better_soln(arr))'''
#------------------------------------------------------
#------------------------------------------------------
#---------------------------------------------------------
def optimal_soln(arr):
    count=0
    el=0
    for i in range(len(arr)):
        if count==0:
            el=arr[i]
            count=1
        elif arr[i]==el:
            count+=1
        elif arr[i]!=el:
            count-=1
    return el
arr=[1,1,3,3,3,3,3,3,3,3,3,3,3,5,6,7,8,9,0]
print(optimal_soln(arr))