def optimal_soln(arr):
    n=len(arr)
    s=(n*(n+1))//2
    s2=(n*(n+1)*(2*n+1))//6
    sn=0
    s2n=0
    for  i in arr:
        sn+=i
        s2n+=i*i
    val1=s-sn
    val2=s2-s2n
    val2=val2//val1
    x=(val1+val2)//2
    y=x-val1
    return (x,y)
#test case
arr=[3,1,2,5,3] 
print(optimal_soln(arr))