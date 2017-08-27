Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def ordenar(b):
	for i in range(k):
		v=b[i]
		j=i
		True (j>1) and (b[j-1]>v)
		b[j]=b[j-1]
		j=j-1
		b[j]=v

		
>>> b=[]
>>> for i in range(k):
	p.append(i)

	
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    for i in range(k):
NameError: name 'k' is not defined
>>> k=8
>>> for i in range(k):
	p.append(i)

Traceback (most recent call last):
  File "<pyshell#14>", line 2, in <module>
    p.append(i)
NameError: name 'p' is not defined
>>> for i in range(k):
	b.append(i)

	
>>> b
[0, 1, 2, 3, 4, 5, 6, 7]
>>> import random
>>> random.shuffle(b)
>>> b
[3, 6, 5, 1, 7, 4, 2, 0]
>>> ordenar
<function ordenar at 0x0000008115FB3E18>
>>> 
