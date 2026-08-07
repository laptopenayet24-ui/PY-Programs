def optimalsoln(arr):
    count1=0
    count2=0
    el1=None
    el2=None
    l=len(arr)
    for i in range(l):
        if count1==0 and arr[i]!=el2:
            count1=1
            el1=arr[i]
        elif count2==0 and arr[i]!=el1:
            count2=1
            el2=arr[i]
        elif arr[i]==el1:
            count1+=1
        elif arr[i]==el2:
            count2+=1
        else:
            count1-=1
            count2-=1
    count1=0
    count2=0
    for i in range(l):
        if arr[i]==el1:
            count1+=1
        elif arr[i]==el2:
            count2+=1
    if count1>=l//3:
        print(el1)
    if count2>=l//3:
        print(el2)
#------------------------------------------------------
arr=[1,2,3,1,1,2,2]
optimalsoln(arr) 