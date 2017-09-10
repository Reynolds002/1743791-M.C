cont=0
def ord_inser(arr):
	global cont
	for ind in range(1,len(arr)):
		valor=arr[ind]
		i=ind-1
		while (i>=0):
			cont+=1
			if (valor < arr[i]):
				arr[i+1]=arr[i]
				arr[i]=valor
				i=i-1
			else:
				break