from turtle import left


def bettersoln1(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    left=n-1
    right=0
    while left>=0 and right<m:
        if arr1[left]>arr2[right]:
            arr1[left],arr2[right]=arr2[right],arr1[left]
            left-=1
            right+=1
        else:
            break
    arr1.sort()
    arr2.sort()
#-----------------------------------------------------------------------------
arr1=[1,3,5,7]
arr2=[0,2,6,8,9]
#-------------------------------------------------------------------------  
def bettersoln2(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    total_len = n + m
    gap = (total_len // 2) + (total_len % 2)
    
    while gap > 0:
        left = 0
        right = left + gap
        
        while right < total_len:
            # CASE 1: Both pointers are in arr1
            if right < n:
                if arr1[left] > arr1[right]:
                    arr1[left], arr1[right] = arr1[right], arr1[left]
            
            # CASE 2: left in arr1, right in arr2
            elif left < n and right >= n:
                if arr1[left] > arr2[right - n]:
                    arr1[left], arr2[right - n] = arr2[right - n], arr1[left]
            
            # CASE 3: Both pointers are in arr2
            else:
                if arr2[left - n] > arr2[right - n]:
                    arr2[left - n], arr2[right - n] = arr2[right - n], arr2[left - n]

            left += 1
            right += 1
        if gap == 1:
            break
        gap = (gap // 2) + (gap % 2)
bettersoln2(arr1, arr2)