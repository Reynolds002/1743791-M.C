cnt=0
def fibonacci(h):
        global cnt
        cnt+=1
        if h==0 or h==1:
                return 1
        return fibonacci(h-2) + fibonacci(h-1)

for i in range(0,51):
	cnt=0
	print(i,fibonacci(i), cnt)
