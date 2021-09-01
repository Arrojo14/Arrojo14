# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 22:28:21 2021

@author: larro
"""

# By definition, protected and private attributes are not part of an interface, even if “protected” is merely a naming convention

# On the other hand, it’s not a sin to have public data attributes as part of the interface of an object, because—if necessary—a data attribute can always be turned into a property implementing getter/setter logic without breaking client code that uses the plain obj.attr syntax

if 1==-1:
    
    class Vector2d:
        
     typecode = 'd'
     
     def __init__(self, x, y):
         self.x = float(x)
         self.y = float(y)
         
     def __iter__(self):
         return (i for i in (self.x, self.y))

# x and y are public data attributes

if 1==-1:
    
    class Vector2d:
        
     typecode = 'd'
     
     def __init__(self, x, y):
         self.__x = float(x)
         self.__y = float(y)
         
     @property
     def x(self):
         return self.__x
    
     @property
     def y(self):
         return self.__y
     
     def __iter__(self):
         return (i for i in (self.x, self.y))
 
# In a newer Vector2d model, we added two properties to make self.x and self.y unmutable, but users can still read my_vector.x and my_vector.y 


if 1==-1:
    
    class Foo:
        
        def __getitem__(self, pos):
            return range(0, 30, 10)[pos]
        
    
    
    f = Foo()
    
    print(f[1])
    
    for i in f: print(i)
    
    print(20 in f)
    
    print(15 in f)



# Given the importance of the sequence protocol, in the absence __iter__ and __contains__ Python still manages to make iteration and the in operator work by invoking __getitem__



if 1==-1:

    import collections
    Card = collections.namedtuple('Card', ['rank', 'suit'])
    
    class FrenchDeck:
        
         ranks = [str(n) for n in range(2, 11)] + list('JQKA')
         suits = 'spades diamonds clubs hearts'.split()
         
         def __init__(self):
             self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
         
         def __len__(self):
             return len(self._cards)
         
         def __getitem__(self, position):
             return self._cards[position]



# Our original FrenchDeck from Chapter 1 does not subclass from abc.Sequence either, but it does implement both methods of the sequence protocol: __getitem__ and __len__.





# The random.shuffle(list) allows us to shuffle, as simple as that

if 1==-1:
    
    from random import shuffle
    l = list(range(10))
    shuffle(l)
    print(l)



# Now let's try to shuffle a FrenchDeck class


if 1==-1:
    
    import collections
    import random
    Card = collections.namedtuple('Card', ['rank', 'suit'])
    
    class FrenchDeckv2:
        
         ranks = [str(n) for n in range(2, 11)] + list('JQKA')
         suits = 'spades diamonds clubs hearts'.split()
         
         def __init__(self):
             self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
         
         def __len__(self):
             return len(self._cards)
         
         def __repr__(self):
             return str(self._cards)
         
         def __getitem__(self, position):
             return self._cards[position]
    
    
    Deck= FrenchDeckv2()
    
    if 1==-1:
        
        print(Deck) # Here we see that the deck is created, so we should be able to shuffle it, right?
        
        print(random.shuffle(Deck)) # '"FrenchDeckv2" object does not support item assignment' The problem is that shuffle operates by swapping items inside the collection, and FrenchDeck only implements the immutable sequence protocol. Mutable sequences must also provide a __setitem__ method.
    
    
    # So let's make a __setitem__ method
    
    
    def set_card(Deck, position, card): # Create a function that takes deck, position, and card as arguments
        
        Deck._cards[position] = card # basically it asigns every namedtuple on the array the "value" of card, so it makes it mutable bc from now you are able to re-sort those cards
        
    
    
    FrenchDeckv2.__setitem__ = set_card # We assgin the set_card as the __setitem__ of the class that will make the deck mutable
    print(random.shuffle(Deck)) # Once this is done we can see that the deck is shuffleale
    print(Deck[:5]) # And we can get slices of it


# The ABCs or abstract base classes can be used to test whether a class provides a particular interface; for example, whether it is hashable or whether it is a mapping.


if 1==-1: # In some cases, even if we havent registered a class for an ABC, we dont need it to be recognised as a subclass
    
    class Struggle:
        def __len__(self): return 23
    
    from collections import abc
    print(isinstance(Struggle(), abc.Sized)) # True, it's recognised as an ABC subclassed



if 1==-1:
    
    import collections
    Card = collections.namedtuple('Card', ['rank', 'suit'])
    
    class FrenchDeck2(collections.MutableSequence): # Ok, so the subclass that we've chosen is an ABC that ensures that our class provides a mutable sequence (the deck in this case)
        
    # An interesting fact of the ABCs is that to ensure that the class do what the subclass indicates, it requires some key functions, in this case it requires __getitem__, __setitem__, __delitem__, __len__, and insert
    
    
         ranks = [str(n) for n in range(2, 11)] + list('JQKA')
         suits = 'spades diamonds clubs hearts'.split()
         
         def __init__(self):
                 self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
         
         def __len__(self): # Seen before, necessary for the subclass, nothing new
             return len(self._cards)
         
         def __getitem__(self, position): # Also seen before and also necessary
             return self._cards[position]
         
         def __setitem__(self, position, card): # Seen before, makes the deck mutable. Also necessary.
             self._cards[position] = card
         
         def __delitem__(self, position): # Not seen before but kinda easy to understand, asks for the same parametters as the getitem but it deletes them instead of returning. Also necessary
             del self._cards[position]
         
         def insert(self, position, card): # New, inserts the card in the position dessired. Also necessary.
             self._cards.insert(position, card)




if 1==-1:
    
    import abc
    
    
    class Tombola(abc.ABC): # Basically this is an abstract class, what's that? A class wich only purpose is to explain real classes with similar structure, an abstract class doesn't work and it's fullfilled of abstract or concrete methods
     
    
         @abc.abstractmethod
         def load(self, iterable): 
             """Add items from an iterable."""
             
         @abc.abstractmethod
         def pick(self): 
             """Remove item at random, returning it.
         This method should raise `LookupError` when the instance is empty.
         """
    
         # Concrete methods on "father" abstract classes are made for the "sons" classes, they will inherit these methods if they haven't got one with the same name already defined
    
    
         def loaded(self): 
             """Return `True` if there's at least 1 item, `False` otherwise."""
             return bool(self.inspect())
         
         def inspect(self):
             """Return a sorted tuple with the items currently inside."""
             items = []
             while True: 
                 try:
                     items.append(self.pick())
                 except LookupError:
                    break
                
             self.load(items) 
             return tuple(sorted(items))
    
    
    # Now let's make a class with Tombola as subclass, remember the new class can only inherit the concrete methods of Tombola, not the abstract ones, but the abstract one need to be implemented as concretes in order to make the class work.
    
    
    
    if 1==-1:
        
        class Fake(Tombola):
            
            def pick(self):
                return 13
        
        print(Fake)  
        
        f = Fake()  # "Can't instantiate abstract class Fake with abstract methods load" What has failed? We haven't implemented the load method.
    
    
    
    # Now let's try again but this time with a properly done class
    
    
    
    import random
    
    class BingoCage(Tombola): 
        
         def __init__(self, items):
             self._randomizer = random.SystemRandom() # random.SystemRandom implements the randomAPI on top of the os.urandom(…) function,which providesrandom bytes “suitable for cryptographic use
             self._items = [] # Initialize a list
             self.load(items)  # Calls the load method in the moment the object is initiated
             
         def load(self, items):
             self._items.extend(items) # Puts the items into the self._items list
             self._randomizer.shuffle(self._items) # Shuffle the self._items
             
         def pick(self): 
             try:
                 return self._items.pop() # Return the last item of self._items
             except IndexError:
                 raise LookupError('pick from empty BingoCage') # Error only rises if items is self._items
                 
         def __call__(self): 
             self.pick() # The moment the object is called, it picks an item
    
    
    
    if 1==-1:
        
        B1 = BingoCage(range(6))
        print(B1._items)
        x = B1.pick()
        print(x)
    
    
    # Let's make a new one but this time redifining the loaded and inspect methods
    
    class LotteryBlower(Tombola):
        
         def __init__(self, iterable):
             self._balls = list(iterable) # Take a look at the fact that we use list(iterable) and not just iterable, this is to make a copy of the list and not depending on an external one
             
         def load(self, iterable):
             self._balls.extend(iterable) # Loads the self._balls with a new set of balls
             
             
         def pick(self):
             
             try:
                 position = random.randrange(len(self._balls)) # We select an index in the range of the list
                 
             except ValueError:
                 raise LookupError('pick from empty BingoCage')
                 
             return self._balls.pop(position)  # The method returns us a random ball of the array by using the index obtained in line 315
         
            
    # Look how both concepts of Tombola use, one shuffles the array and returns always the last position the other one just selects a random position of the array and returns it
         
    
         def loaded(self): 
             return bool(self._balls) # True if the list self._balls is not empty, False if it's empty
         
         def inspect(self): 
             return tuple(sorted(self._balls)) # Just returns a  sorted tuple of self._balls
    
    
    if 1==-1:
        
        l1 = LotteryBlower(range(9))
        print(l1._balls)
        l1.load(range(9,14))
        print(l1._balls)
    
    
    
    
    @Tombola.register # We register Tombolist as a subclass of Tombola
    class TomboList(list): # It extends list
        
         def pick(self):
             if self:
                 position = random.randrange(len(self)) # Picks a random position in the range of the array
                 return self.pop(position) # Returns the item that is on that position
             else:
                 raise LookupError('pop from empty TomboList')
                 
         load = list.extend # Tombolist.load is the same as Tombolist.list.extend
         
         def loaded(self):
             return bool(self) # Tombolist inherits __bool__ from list
         
         def inspect(self):
             return tuple(sorted(self)) # same as before, but because self is a list itself, we don't need no self._balls
    
    
    
    # We have some different models of Tombola. But can we test them in one attempt to see if there's anyone that doesn't work? Yes we can, let's do it
    
    
    
    
    import doctest
    
    
    TEST_FILE = 'tombola_tests.rst'
    TEST_MSG = '{0:16} {1.attempted:2} tests, {1.failed:2} failed - {2}'
    
    def main(argv):
         verbose = '-v' in argv
         subclasses = Tombola.__subclasses__()
    
         for cls in subclasses: 
             test(cls, verbose)
    
    
    def test(cls, verbose=False):
        
         res = doctest.testfile(
         TEST_FILE,
         globs={'ConcreteTombola': cls}, 
         verbose=verbose,
         optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
         
         tag = 'FAIL' if res.failed else 'OK'
         print(TEST_MSG.format(cls.__name__, res, tag))
       
       
    
    if __name__ == '__main__':
        import sys
        main(sys.argv)
    
    
    
    # Well, this crash and i don't really know why.




if 1==-1:
    
    class Struggle:
        def __len__(self): return 23
    
    from collections import abc
    
    print(isinstance(Struggle(), abc.Sized)) # Becayse Struggle is an abc.Sized type, it's true
    
    print(issubclass(Struggle, abc.Sized)) # Because Struggle is a subclass of abc, the function turns out to be true
    




if 1==-1:

    class DoppelDict(dict): # The subclass indicates the type in which the object is built in, in this case, self will be a dict
        def __setitem__(self, key, value):
            super().__setitem__(key, [value] * 2) # Super refers to the father class (dict in this case), uses it's __setitem__ method and duplicates values when storing for no reason xDD
    
    dd = DoppelDict(one=1) # The __init__ method inherited from dict clearly ignored that __setitem__ was overridden: the value of 'one' is not duplicated
    print(dd)
    
    dd['two'] = 2 # This clearly makes use of the __setitem__ method and works as expected
    print(dd)
    
    dd.update(three=3) # The __init__ method inherited from dict clearly ignored that __setitem__ was overridden: the value of 'one' is not duplicated
    print(dd)




if 1==-1:
    class AnswerDict(dict):
        def __getitem__(self, key):
            return 42 # We create another class with disct as subclass and just redifine __getitem__, it will only return 42 if activated
    
    ad = AnswerDict(a='foo') # We create an AnswerDict {a:"foo"}
    print(ad['a']) # 42. Why do we receive 42? Because the new __getitem__ method has been activated and it only returns 42
    print(ad) # We get the dictionary because __getitem__ hasn't been activated
    
    d = {} # But let's create a dictionary
    d.update(ad) # And let's add to this new dictionary the AnswerDict created before {a:"foo"}
    
    print(d['a']) # foo. Now we are getting the desired answer why? Because the __getitem__ we have invoked now is the __getitem__ of the father class
    print(d) # And there you have your dictionary




if 1==-1:
    import collections
    
    class DoppelDict2(collections.UserDict): # First of all, why using collections.UserDict instead of dict? because you can inherit from dict but you'll have to override every single method of interest, instead the UserDict goes back a lot further and lets you implement just a few methods
        def __setitem__(self, key, value): # We just want to modify the __setitem__
            super().__setitem__(key, [value] * 2) # The super calls the father function's (UserDict) __setitem__ and modifies only the [value]
    
    dd = DoppelDict2(one=1)
    print(dd)
    
    dd['two'] = 2
    print(dd)
    
    dd.update(three=3)
    print(dd)




if 1==-1:
    
    class AnswerDict2(collections.UserDict):
        def __getitem__(self, key):
            return 42
    
    ad = AnswerDict2(a='foo')
    print(ad['a']) # 42 as expected, nothing new
    
    d = {} # we create a dictionary
    d.update(ad) # we add to it the ad {'a': 'foo'}
    print(d['a']) # But we receive 42 instead of foo, why?
    
    print(d) # {'a': 42} foo has been replaced with 42 in the new dict, but let's see if ad is still {'a': 'foo'} 
    print(ad) # It is, what has happenned is that when adding ad to d, the UserDict has replaced foo with 42 because of the new __getitem__



# All of them worked as we wanted this time, the modified __setitem__ and __getitem__ have been activated in every single case. But why?
# As explained above, the UserDict is much better than the dict as subsclass because it lets you implement just a few methods and make them effective for the whole class




# When inheriting classes we face the problem of the order, in this example we will learn about the diamond problem, which shows the conflicts when unrelated ancestor classes implement a method by the same name

if 1==-1:
    
    class A: # We create a class named A, nothing too complicated
         def ping(self): # And create a method named "ping"
             print('ping:', self) # It pings the proper class
    
        
    # Now let's put A as a subclass in B and C and create a "pong" method in both 
    
    class B(A): 
         def pong(self):
             print('pong:', self)
         
    class C(A):
         def pong(self):
             print('PONG:', self)
         
    # Finally let's use B and C as subclasses for D, and let's see if it uses B or C when pong is called
         
    
    class D(B, C):
        
         def ping(self):
             super().ping()
             print('post-ping:', self)
             
         def pingpong(self):
             self.ping()
             super().ping()
             self.pong()
             super().pong()
             C.pong(self)
         
    if 1==-1:
        
        d = D()
        
        print(d.pong()) # pong: <__main__.D object at 0x000001F542619520>   It uses the B one!
        print(C.pong(d)) # You can call a method on a superclass directly, passing the instance as an explicit argument
    
    
    # The MRO, Method Resolution Order indicates the order that a class follows in order to implement a method
    
    if 1==-1:
        print(D.__mro__) # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>) and we can see that B is over C, so if both classes have a similar method, B will be always preferred
    
    
    # However, it’s also possible, and sometimes convenient, to bypass the MRO and invoke a method on a superclass directly. For example, the D.ping method could be written as:
    
        
    def ping(self):
        A.ping(self) # instead of super().ping()
        print('post-ping:', self)
    
    D.ping = ping
    
    if 1==-1:
        
        d = D()
        d.ping()
        # ping: <diamond.D object at 0x10cc40630>
        # post-ping: <diamond.D object at 0x10cc40630>
    
    
    if 1==-1:
        
        d=D()
        d.pingpong()
        
        # Now let's explain what happens in d.pingpong
        
        def pingpong(self):
            
            self.ping() # Activates D.ping() which first calls ping in A and after that prints a post-ping in D
            super().ping() # Activates ping in A
            self.pong() # Activates pong in B
            super().pong() # Activates pong in B again
            C.pong(self) # Bypassing the MRO we call pong in C



# If we inspect the MRO of some Python original classes, we can observe that most of them have multiple subclasses

print(bool.__mro__) 

def print_mro(func):
    for i in func.__mro__:
        print (i.__name__, end = " ")
    print("")


import numbers
print_mro(numbers.Integral) # These are the numeric ABCs provided by the numbers module.

import io 
print_mro(io.BytesIO)
print_mro(io.TextIOWrapper)

# The io module includes ABCs (those with the …Base suffix) and concrete classes like BytesIO and TextIOWrapper, which are the types of binary and text file objects returned by open(), depending on the mode argument