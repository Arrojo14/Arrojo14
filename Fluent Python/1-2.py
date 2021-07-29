# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 11:47:03 2021

@author: larro
"""
if 3==2:
    import collections
    
    Card= collections.namedtuple("Card",["rank","suit"])
    
    class FrenchDeck:
        
        ranks= [str(n) for n in range(2,11)]+list("JQKA")
        suits= "Hearts Diamonds Clubs Hearts".split()
    
        def __init__(self):
            self._cards= [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        def __len__(self):
            return len(self._cards)
        def __getitem__(self, position):
            return self._cards[position]
    
    deck=FrenchDeck()
    print(len(deck))
    
    sietediamantes = Card("7","diamonds")
    print(sietediamantes)
    
    print(deck[2])
    
    import random
    
    print(random.choice(deck))
    
    print(Card("3","Hearts") in deck)
    print(sietediamantes.rank)
    
if 3==2:
    from math import hypot
    
    class Vector:
        
        def __init__(self,x,y):
            self.x=x
            self.y=y
            
        def __repr__(self):
            return 'Vector(%r, %r)' % (self.x, self.y)
        
        def __abs__(self):
            return hypot(self.x, self.y)
        
        def __bool__(self):
            return bool(abs(self))
    
        def __add__(self,other):
            x=self.x+other.x
            y=self.y+other.y
            return Vector(x,y)
    
        def __mul__(self,n):
            x=self.x*n
            y=self.y*n
            return Vector(x,y)
        
        
    
    v1= Vector(0,0)
    v2 = Vector(0,0)
    v3=v1+v2
    print(v3*2)
        
        
if 3==2:
      
    Niveles= ["1","2","3"]
    Dificultades= ["Easy","Medium","Hard"]
    
    Combinaciones= ["%s %s" % (df,lvl) for df in Dificultades for lvl in Niveles]
    for i in Combinaciones:
        print(i)
    
    for n in Dificultades:
        for i in Niveles:
            print("%s %s." % (n,i),end=" ")
    print()


if 3==2:
    
    symbols = '$¢£¥€¤'  
    x=tuple(ord(symbol) for symbol in symbols)
    print(x)
    
    
if 3==2:
    a, *body, c, d = range(5)
    print(a, body, c, d)
    
    a, *body, c, d = range(5)
    print(a, *body, c, d)
    

if 3==2:
    mix=[1,2,3,4,5,6,7,8] 
    print(mix[:2])   # Imprime posiciones 0-1
    print(mix[2:])   # Imprime posiciones a partir de la 2 (incluida)
    print(mix[::-1])  # Invierte cadena
    print(mix[::2])  # Salta de 2 en 2
    print(mix[2:5])  # Se queda con las posiciones 2-3-4
    print(mix[3::2])  # Salta de 2 en 2 a partir de la pos 3 (incluida)
    mix[2:5]=[100]   # Convierte las posiciones 2-3-4 en un 100
    print(mix)
    mix=[1,2,3,4,5,6,7,8]
    print(mix*3)   # Triplica la cadena


if 3==2:
    a=["_"]*3  # Esta es la manera en la que me enseñaron
    for i in range (3):
        a[i]=["_"]*3
    print(a)
    
    b=[["_"]*3]*3 # Esta la vista en el libro
    
    a[1][2]="O"
    print(a)
    
    b[1][2]="O" # La manera vista en el libro no me convence, pues la única coordenada significativa es la segunda.
    print(b)


if 3==2:
    l = [1, 2, 3]
    print(id(l))
    
    l *= 2
    print(l)
    
    t = (1, 2, 3)
    print(id(t))
    
    t *= 2
    print(id(t))


# En caso de tener una lista a y una b, no sería idóneo a[i] += b

#key=método ordenanza, #reverse=True/False


if 3==2:
    fruits = ['grape', 'raspberry', 'apple', 'banana']
    print(sorted(fruits,key=len,reverse=True))
    
    
if 3==2: # Uso bisect
    import bisect
    a=[2,20,31,35,37,55]
    x=bisect.bisect_left(a,31)
    bisect.insort_right(a,31)
    print(x)
    print(a)


# El ejemplo para el uso de Bisect es innecesariamente extenso en el libro, crearé uno más sencillo pero con similar uso del bisect.

if 3==2:
    
    import bisect
    
    a = [31,4,27,3,57,89,2,70,1]
    b=[]
    fmt="{:9}{:9}"
    print(fmt.format("Posición","Cadena"))
    for i in a:
        x=bisect.bisect_left(b,i)
        bisect.insort_left(b,i)
        print(" "*4,x, end=" "*4)
        print(b)


# Voy a intentar el 2-18 sin mirar el libro a ver cómo sale


if 3==2:    
    import bisect
    
    marks=[0,1,2,3,4,5,6,7,8,9,10]
    
    mark=int(input("Introduce mark: "))
    while mark<0 or mark>10:
        print("Invalid mark")
        mark=int(input("Introduce mark: "))
        
    x=bisect.bisect_left(marks,mark)
    
    if x>=9:
        print("A")
        
    elif x>=7:
        print("B")
    
    elif x>=5:
        print("C")
    
    else:
        print("D")


# El enfoque es muy distinto, pero estoy bastante satisfecho con mi modelo.

if 3==2:
    
    import bisect
    
    def grade(score,marcas=[60,70,80,90],grades="FDCBA"):
        x=bisect.bisect_right(marcas,score)
        return(grades[x])
        
    x=[]    
    x += (grade(score) for score in [33, 99, 77, 70, 89, 90, 100])
    print(x)



if 3==2: # EL autor recalca que ordenar las listas consume excesiva memoria, por lo que el uso del bisect será fundamental.
    import bisect
    import random
    
    random.seed(1729)
    
    my_list = []
    
    for i in range(7):
        x=random.randrange(14)
        bisect.insort(my_list,x)
        print ("%2d->" % x,my_list) 
    
if 3==2: #Se crea un array x de 10^7 número aleatorios, se guarda como archivo binario, y se crea una copia en otro array x2
    from array import array
    from random import random
    
    x=array("d", (random() for i in range(10**7)))
    y=open("x.bin","wb")
    x.tofile(y)
    y.close()
    x2=array("d")
    y=open("x.bin","rb")
    x2.fromfile(y,10**7)
    if x==x2:
        print("yes")


if 3==2: # Se crea una ventana al array original por medio de memoryview
    from array import array
    
    x=array("h",[-2,-1,0,1,2])
    y=memoryview(x)
    cast=y.cast("B")
    cast.tolist()
    cast[5]=4
    print(x)
    

if 3==2: #Uso násico de matrices numpy    
    import numpy
    
    a = numpy.arange(12)
    print(a)
    print(type(a))
    
    a.shape = 3,4 # Elegir tamaño matriz
    print(a)
    print(a[2]) #Filas
    print(a[:,2]) #Columnas
    print(a.transpose()) #Transformar la matriz


if 3==2:
    import numpy
    
    
    floats = numpy.loadtxt('floats-10M-lines.txt') 
    floats[-3:] 
    floats *= .5 
    floats[-3:]
    
    from time import perf_counter as pc
    t0 = pc(); floats /= 3; pc() - t0
    
    numpy.save('floats-10M', floats) 
    floats2 = numpy.load('floats-10M.npy', 'r+') 
    floats2 *= 6
    floats2[-3:]


if 3==2:
    import collections
    
    dq= collections.deque(range(10),maxlen=10)
    print(dq)
    dq.pop()
    dq.popleft()
    dq.append("Derecha")
    dq.appendleft("Izquierda")
    print(dq)
    # También tenemos el .extend para poner números extras en orden ascendente y el .rotate(num) para rotar hacia el lado deseado las casillas preferidas 
    














