def countunique_items(arr):
    i=0
    for j in range(i+1,len(arr)):
        if arr[i]!=arr[j]:
            arr[i+1]=arr[j]
            i+=1
    return i+1
#------------------------------------------------------------------
l=[1,1,1,2,2,3,4,4,5]
print(countunique_items(l))