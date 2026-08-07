def movingzeros(arr):
    a=0
    for i in range(len(arr)):
        if arr[i]==0:
            a=i
            break
        else:
            print("No zeros found in the array")
            return arr
    i=a
    for j in range(i+1,len(arr)):
        if arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    return arr
#-------------------------------------------------------------------
l=[1,2,3,4,5,6,7,8]
print(movingzeros(l))