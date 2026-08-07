def rmdup(arr):
    l=[]
    for i in arr:
        if i not in l:
            l.append(i)
    return l
#___________-------------------------------------------_____________
arr=[1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4]
print(rmdup(arr))