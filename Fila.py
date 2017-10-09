class fila:
    def __init__(self):
        self.fila=[]
    def obtener (self):
        return self.fila.pop()
    def meter (self,e):
        self.fila.append(e)
        return len(self.fila)
    @property
    def longitud (self):
        return len(self.fila)
p=fila()
p.meter(1)
p.meter(2)
p.meter(3)
p.meter(4)
print(p.longitud)
print(p.obtener())
print(p.obtener())
