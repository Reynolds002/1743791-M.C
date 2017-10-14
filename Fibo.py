cnt=0
def fibo(h):
	w=0
	w1=1
	w2=1
	global cnt
	if h==0 or h==1:
		return 1
	for i in range(2,h+1):
		cnt+=1
		w=w1+w2
		w2=w1
		w1=w
	return w

for h in range (0,43):
	cnt=0
	print(h,fibo(h), cnt)	
