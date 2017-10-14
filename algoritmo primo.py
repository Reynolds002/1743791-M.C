cnt=0
print("El progama dira si no es primo de lo contrario solo pondra el numero ingresado y el numero de operaciones")
def primo(n):
    #print("El progama dira si no es primo de lo contrario solo pondra el numero ingresado y el numero de operaciones")
    cnt=0
    for i in range(2,n):
        cnt=cnt+1
        if((n%i)==0):
            if(n%n==0):
                print("no es primo")
                break
            else:
                print("es primo")
               
            
            
    return n,cnt





