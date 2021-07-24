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
    




































