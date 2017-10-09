class pila:
    def __init__(self):
        self.pila=[]
    def obtener (self):
        return self.pila.pop()
    def meter (self,e):
        self.pila.append(e)
        return len(self.pila)
    @property
    def longitud (self):
        return len(self.pila)
x=9
p=pila()
p.meter(1)
p.meter(2)
p.meter(x)
p.meter(x*2)
print(p.longitud)
print(p.obtener())
print(p.obtener())
