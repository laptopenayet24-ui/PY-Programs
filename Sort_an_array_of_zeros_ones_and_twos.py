arr=[1,0,0,0,1,1,1,2,2,2,0,0,1]
def better_sort(arr):
    c0=c1=c2=0
    for i in arr:
        if i==1:
            c1+=1
        elif i==0:
            c0+=1
        elif i==2:
            c2+=1
    for i in range(c0):
        arr[i]=0
    for i in range(c1):
        arr[c0+i]=1
    for i in range(c2):
        arr[c0+c1+i]=2
#________________________________________________________________________
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#__________________________________________________________________________
def optimal_sort(arr):
    low=0
    mid=0
    high=len(arr)-1
    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        elif arr[mid]==2:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1

#--------------------------------------------------------------------------
'''better_sort(arr)
print(arr)'''
optimal_sort(arr)
print(arr)