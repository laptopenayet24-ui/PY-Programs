''' longest  consecutive sequence
arr=[102,4,100,1,101,3,2,1,1,]  here the answer is 4
''' 
def better_soln(arr):
	count=0
	max_count=0
	last_min=float('-inf')
	s_arr=sorted(arr)
	l=len(s_arr)
	for i in range(l):
		if s_arr[i]==last_min+1:
			last_min=s_arr[i]
			count+=1
		elif s_arr[i]>last_min+1:
			last_min=s_arr[i]
			count=1
		max_count=max(max_count,count)
	return max_count
#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
arr=[102,4,100,1,101,3,2,1,1,]
#-------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
def optimal_soln(arr):
	s_arr=set(arr)
	max_count=0
	for i in s_arr:
		if i-1 not in s_arr:
			count=1
			while i+1 in s_arr:
				count+=1
				i+=1
				max_count=max(max_count,count)
	return max_count
#-------------------------------------------------------
print(optimal_soln(arr))