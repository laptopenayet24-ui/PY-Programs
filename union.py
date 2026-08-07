def unioin(lst1,lst2):
    lst3=[]
    j=0
    for  i in range(len(lst1)):
        if lst1[i] not in lst3 and lst1[i]<=lst2[j]:
            lst3.append(lst1[i])
        else:
            lst3.append(lst2[j])
            j+=1
            i-=1
    return lst3
#---------------------------------------------------------------    
l1=[1,2,3,4,5,6]
l2=[4,5,6,7,8,9]
print(unioin(l1,l2))
