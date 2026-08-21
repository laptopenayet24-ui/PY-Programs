def optimal_soln(arr):
    n = len(arr)
    ans = float('inf')
    low, high = 0, n - 1

    while low <= high:
        # If search space is already sorted, min is arr[low]
        if arr[low] <= arr[high]:
            return min(ans, arr[low])

        mid = (low + high) // 2

        if arr[low] <= arr[mid]:  # Left half is sorted
            ans = min(ans, arr[low])
            low = mid + 1
        else:                     # Right half is sorted
            ans = min(ans, arr[mid])
            high = mid - 1        

    return ans


#