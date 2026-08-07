def seprate(arr):
    ret_arr=[0]*len(arr)
    pos_index=0
    neg_index=0
    size=len(arr)
    for i in range(size):
        if arr[i]>=0:
            ret_arr[2*pos_index]=arr[i]
            pos_index+=1
        else:
            ret_arr[2*neg_index+1]=arr[i]
            neg_index+=1
    return ret_arr
#--------------------------------------------------------------------
arr=[-1,-2,-3,1,2,3]
print(seprate(arr))