arr1=[]
arr2=[]
arr3=[]
arr4=[]
arr5=[]
arr6=[]
arr7=[]
arr8=[]
arr9=[]
arr10=[]
arr11=[]
arr12=[]
arr13=[]
arr14=[]
arr15=[]
arr16=[]
arr17=[]
arr18=[]
arr19=[]
arr20=[]
arr21=[]
arr22=[]
arr23=[]
arr24=[]
arr25=[]
arr26=[]
arr27=[]
arr28=[]
arr29=[]
arr30=[]
cnt1=0
cnt2=0
cnt3=0
cnt4=0
arr=[]
for i in range(1,200,2):
	arr1.append(i)
for i in range(1,300,3):
	arr2.append(i)
for i in range(1,400,4):
	arr3.append(i)	
for i in range(1,500,5):
	arr4.append(i)
for i in range(1,600,6):
	arr5.append(i)	
for i in range(1,700,7):
	arr6.append(i)
for i in range(1,800,8):
	arr7.append(i)
for i in range(1,900,2):
	arr8.append(i)
for i in range(1,100,10):
	arr9.append(i)
for i in range(1,200,3):
	arr10.append(i)
for i in range(1,230,4):
	arr11.append(i)
for i in range(1,250,4):
	arr12.append(i)
for i in range(1,290,4):
	arr13.append(i)
for i in range(1,600,8):
	arr14.append(i)
for i in range(1,400,3):
	arr15.append(i)
for i in range(1,550,5):
	arr16.append(i)
for i in range(1,330,3):
	arr17.append(i)
for i in range(1,648,4):
	arr18.append(i)
for i in range(1,505,5):
	arr19.append(i)
for i in range(1,666,6):
	arr20.append(i)
for i in range(1,333,3):
	arr21.append(i)
for i in range(1,345,9):
	arr22.append(i)
for i in range(1,749,3):
	arr23.append(i)
for i in range(1,268,2):
	arr24.append(i)
for i in range(1,300,3):
	arr25.append(i)
for i in range(1,300,3):
	arr26.append(i)
for i in range(1,300,3):
	arr27.append(i)
for i in range(1,300,3):
	arr28.append(i)
for i in range(1,300,3):
	arr29.append(i)
for i in range(1,999,9):
	arr30.append(i)	
	
import random
random.shuffle(arr1)
random.shuffle(arr2)
random.shuffle(arr3)
random.shuffle(arr4)
random.shuffle(arr5)
random.shuffle(arr6)
random.shuffle(arr7)
random.shuffle(arr8)
random.shuffle(arr9)
random.shuffle(arr10)
random.shuffle(arr11)
random.shuffle(arr12)
random.shuffle(arr13)
random.shuffle(arr14)
random.shuffle(arr15)
random.shuffle(arr15)
random.shuffle(arr16)
random.shuffle(arr17)
random.shuffle(arr18)
random.shuffle(arr19)
random.shuffle(arr20)
random.shuffle(arr21)
random.shuffle(arr22)
random.shuffle(arr23)
random.shuffle(arr24)
random.shuffle(arr25)
random.shuffle(arr26)
random.shuffle(arr27)
random.shuffle(arr28)
random.shuffle(arr29)
random.shuffle(arr30)



def bubble(R):
        global cnt1
        for u in range(1,len(R)-1):
                        for v in range (0,len(R)-u):
                                cnt1+=1
                                if (R[v+1]<R[v]):
                                        repuesto=R[v]
                                        R[v]=R[v+1]
                                        R[v+1]=repuesto
                                        
def ord_inser(arr):
	global cnt2
	for ind in range(1,len(arr)):
		valor=arr[ind]
		i=ind-1
		while (i>=0):
			cnt2+=1
			if (valor < arr[i]):
				arr[i+1]=arr[i]
				arr[i]=valor
				i=i-1
			else:
				break

def selection(arr):
	global cnt3
	for i in range(0,len(arr)-1):
		val=i
		for j in range(i+1,len(arr)):
			(cnt3)+=1
			if (arr[j]<arr[val]):
				val=j
		if(val!=i):
			aux=arr[i]
			arr[i]=arr[val]
			arr[val]=aux
	return arr

def quicksort(arr):
	global cnt4
	if len(arr)<=1:
		return arr
	p= arr.pop(0)
	menores,mayores=[],[]
	for e in arr:
		cnt4+=1
		if e <=p:
			menores.append(e)
		else:
			mayores.append(e)
	return quicksort(menores) + [p] + quicksort(mayores)


print("Resultados numero de operaciones")
print("bubble_insercion_selection_quicksort")
bubble(arr1)
ord_inser(arr2)
selection(arr3)
quicksort(arr4)
print(cnt1,cnt2,cnt3 ,cnt4)
bubble(arr5)
ord_inser(arr6)
selection(arr7)
quicksort(arr8)
print(cnt1,cnt2,cnt3,cnt4)
bubble(arr9)
ord_inser(arr10)
selection(arr11)
quicksort(arr12)
print(cnt1,cnt2,cnt3,cnt4)
bubble(arr13)
ord_inser(arr14)
selection(arr15)
quicksort(arr16)
print(cnt1,cnt2,cnt3,cnt4)
bubble(arr17)
ord_inser(arr18)
selection(arr19)
quicksort(arr20)
print(cnt1,cnt2,cnt3,cnt4)
bubble(arr21)
ord_inser(arr22)
selection(arr23)
quicksort(arr24)
print(cnt1,cnt2,cnt3,cnt4)
bubble(arr25)
ord_inser(arr26)
selection(arr27)
quicksort(arr28)
print(cnt1,cnt2,cnt3,cnt4) 
