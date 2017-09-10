def selection(arr):
	contador=0
	for i in range(0,len(arr)-1):
		val=i
		for j in range(i+1,len(arr)):
			cont+=1
			if (arr[j]<arr[val]):
				val=j
				if (val!=i):
					aux=arr[i]
					arr[i]=arr[val]
					arr[val]=aux
		return arr
				