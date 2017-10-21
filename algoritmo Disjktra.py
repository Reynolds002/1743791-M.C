from heapq import heappop, heappush

def flatten(L):
    while len(L) > 0:
        yield L[0]
        L = L[1]
class Grafo:
 
    def __init__(self):
        self.V = set() # un conjunto
        self.E = dict() # un mapeo de pesos de aristas
        self.vecinos = dict() # un mapeo
 
    def agrega(self, v):
        self.V.add(v)
        if not v in self.vecinos: # vecindad de v
            self.vecinos[v] = set() # inicialmente no tiene nada
 
    def conecta(self, v, u, peso=1):
        self.agrega(v)
        self.agrega(u)
        self.E[(v, u)] = self.E[(u, v)] = peso # en ambos sentidos
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)
 
    def complemento(self):
        comp= Grafo()
        for v in self.V:
            for w in self.V:
                if v != w and (v, w) not in self.E:
                    comp.conecta(v, w, 1)
        return comp

    def shortest(self, v): # Dijkstra's algorithm
        q = [(0, v, ())] # arreglo "q" de las "Tuplas" de lo que se va a almacenar dondo 0 es la distancia, v el nodo y () el "camino" hacia el
        dist = dict() #diccionario de distancias 
        visited = set() #Conjunto de visitados
        while len(q) > 0: #mientras exista un nodo pendiente
            (l, u, p) = heappop(q) # Se toma la tupla con la distancia menor
            if u not in visited: # si no lo hemos visitado
                visited.add(u) #se agrega a visitados
                dist[u] = (l,u,list(flatten(p))[::-1] + [u])  	#agrega al diccionario
            p = (u, p) #Tupla del nodo y el camino
            for n in self.vecinos[u]: #Para cada hijo del nodo actual
                if n not in visited: #si no lo hemos visitado
                    el = self.E[(u,n)] #se toma la distancia del nodo acutal hacia el nodo hijo
                    heappush(q, (l + el, n, p)) #Se agrega al arreglo "q" la distancia actual mas la ditanacia hacia el nodo hijo, el nodo hijo n hacia donde se va, y el camino
        return dist #regresa el diccionario de distancias
#Grafo base
g= Grafo()
g.conecta('a','b', 1)
g.conecta('a','c', 1)
g.conecta('a','d', 1)
g.conecta('a','d', 1)
g.conecta('c','e', 1)
g.conecta('c','f', 10)
g.conecta('b','f', 1)
print(g.shortest('c'))

print("Grafo de 5 nodos y 10 aristas")
h= Grafo()
h.conecta('a','c', 1)
h.conecta('a','b', 3)
h.conecta('a','e', 5)
h.conecta('a','d', 7)
h.conecta('b','d', 9)
h.conecta('b','e', 11)
h.conecta('b','c', 13)
h.conecta('c','e', 17)
h.conecta('c','d', 19)
h.conecta('e','d', 23)
print(h.shortest('d'))

print("grafo de 10 nodos y 20 aristas")
k= Grafo()
k.conecta('a','e', 2)
k.conecta('a','b', 5)
k.conecta('a','f', 3)
k.conecta('b','d', 9)
k.conecta('b','f', 6)
k.conecta('b','g', 1)
k.conecta('b','c', 17)
k.conecta('c','d', 7)
k.conecta('c','g', 4)
k.conecta('c','h', 21)
k.conecta('d','h', 11)
k.conecta('d','i', 8)
k.conecta('d','e', 10)
k.conecta('e','i', 22)
k.conecta('e','j', 25)
k.conecta('f','g', 23)
k.conecta('f','j', 16)
k.conecta('g','h', 17)
k.conecta('h','i', 12)
k.conecta('i','j', 13)
print(k.shortest('a'))

print("grafo de 15 nodos y 30 aristas")
x= Grafo()
x.conecta('a','e', 29)
x.conecta('a','f', 18)
x.conecta('a','b', 1)
x.conecta('b','f', 10)
x.conecta('b','g', 13)
x.conecta('b','c', 9)
x.conecta('c','g', 19)
x.conecta('c','h', 25)
x.conecta('c','d', 28)
x.conecta('d','h', 30)
x.conecta('e','i', 15)
x.conecta('e','j', 5)
x.conecta('e','f', 2)
x.conecta('f','j', 7)
x.conecta('f','k', 8)
x.conecta('f','g', 20)
x.conecta('g','k', 26)
x.conecta('g','l', 23)
x.conecta('g','h', 14)
x.conecta('h','l', 17)
x.conecta('i','m', 12)
x.conecta('i','n', 4)
x.conecta('i','j', 11)
x.conecta('j','n', 21)
x.conecta('j','o', 22)
x.conecta('j','k', 3)
x.conecta('k','o', 6)
x.conecta('k','l', 16)
x.conecta('m','n', 24)
x.conecta('n','o', 27)
print(x.shortest('l'))

print("grafo de 20 nodos y 40 aristas")
y= Grafo()
y.conecta('a','k', 1)
y.conecta('a','b', 2)
y.conecta('a','l', 3)
y.conecta('b','l', 4)
y.conecta('b','m', 5)
y.conecta('b','c', 6)
y.conecta('b','j', 7)
y.conecta('c','m', 8)
y.conecta('c','d', 9)
y.conecta('d','m', 10)
y.conecta('d','n', 11)
y.conecta('d','e', 12)
y.conecta('e','n', 13)
y.conecta('e','o', 14)
y.conecta('e','p', 15)
y.conecta('e','f', 16)
y.conecta('f','p', 17)
y.conecta('f','g', 18)
y.conecta('g','p', 19)
y.conecta('g','h', 20)
y.conecta('h','p', 21)
y.conecta('h','q', 22)
y.conecta('h','r', 23)
y.conecta('h','i', 24)
y.conecta('i','r', 25)
y.conecta('i','s', 26)
y.conecta('i','j', 27)
y.conecta('j','s', 28)
y.conecta('j','t', 29)
y.conecta('j','k', 30)
y.conecta('k','t', 31)
y.conecta('l','t', 32)
y.conecta('l','m', 33)
y.conecta('m','n', 34)
y.conecta('n','o', 35)
y.conecta('o','p', 36)
y.conecta('p','q', 37)
y.conecta('q','r', 38)
y.conecta('r','s', 39)
y.conecta('s','t', 40)
print(y.shortest('p'))









