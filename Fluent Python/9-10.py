# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 10:33:11 2021

@author: larro
"""

if 1==-1:

    from array import array
    import math
    
    
    class Vector2d:
        
            typecode = 'd' # typecode is a class attribute we’ll use when converting Vector2d instances to/from bytes.
    
            
            def __init__(self, x, y):
                self.x = float(x) # We define the x
                self.y = float(y) # # We define the y
            
            # Converting to float early can catch errors early
            
            def __iter__(self): # __iter__ makes a Vector2d iterable
                return (i for i in (self.x, self.y)) 
            
            def __repr__(self): # Returns an str in they way we want, but the __str__ function has priority if we print
                class_name = type(self).__name__
                return '{}({!r}, {!r})'.format(class_name, *self) 
            
            def __str__(self): # Returns an str in they way we want
                return str(tuple(self))
            
            def __bytes__(self):
                return (bytes([ord(self.typecode)]) # Converts to bytes the unicode of the typecode, which is "d"
                + bytes(array(self.typecode, self))) # Converts to bytes the array formed by the unicode and the coordinates
            
            def __eq__(self, other): # Allows us to make easy comparations
                return tuple(self) == tuple(other) 
            
            def __abs__(self):
                return math.hypot(self.x, self.y) # Calculates the module of the vector
            
            def __bool__(self): 
                return bool(abs(self)) # Returns a True unless the number is 0.0
            
            @classmethod # Class method is modified by the classmethod decorator.
            
            def frombytes(cls, octets): # No self argument; instead, the class itself is passed as cls
                typecode = chr(octets[0]) # Read the typecode from the first byte
                memv = memoryview(octets[1:]).cast(typecode) # Create a memoryview from the octets binary sequence and use the typecode to cast it
                return cls(*memv) # Unpack the memoryview resulting from the cast into the pair of arguments needed for the constructor
            
            
            
    
    v1=Vector2d(2,3)
    print(v1)
    print(repr(v1))
    
    x,y=v1 # A Vector2d can be unpacked to a tuple of variables.
    print(x,y)
    
    c=[2,3]
    print(v1==c)
    
    print(bool(v1), bool(Vector2d(0,0))) # The second one is false because it's 0
    
    print(Vector2d.frombytes(bytes(v1))) # The class method works perfectly




if 1==-1:
    
    class Demo:
        @classmethod
        def klassmeth(*args):
            return args
        @staticmethod
        def statmeth(*args):
            return args
    
    print(Demo.klassmeth()) # (<class '__main__.Demo'>,) receives the class
    
    print(Demo.klassmeth('spam')) # (<class '__main__.Demo'>, 'spam') receives the class and an argument
    
    print(Demo.statmeth()) # Receives nothing
    
    print(Demo.statmeth('spam')) # Receives the argument
    
    # What we can get out of this is that statmeth is not really usefull, and a simple function can replace it, but classmethod can be, and we'll see more asbout it in the next exercises
    


if -1==1:
    
    brl = 1/2.43 # BRL to USD currency conversion rate
    print(brl)
    
    print(format(brl, '0.4f')) # We specify only 4 decimal numbers with the format(x, format)
    
    print('1 BRL = {rate:0.2f} USD'.format(rate=brl)) # We can specify the rate and format
    
    print(format(42, 'b')) # Print in binary

    print(format(2/3, '.1%')) # Print in percentage with 1 decimal



if 1==-1:
    
    from datetime import datetime
    
    now = datetime.now() # We get the actual hour
    
    print(format(now, '%H:%M:%S')) # We set the format, but it's mandatory to use the exact same letters in order for it to work
    
    print("It's now {:%H:%M %p}".format(now))



if 1==-1:
    
    # We introduce the __format__ method inside the Vector2d class, so we can implement formats on numbers
    
    def __format__(self, fmt_spec=''):
        components = (format(c, fmt_spec) for c in self) # We apply the format for every c in self, which are self.x and self.y and store them on components
        return '({}, {})'.format(*components) # Once we have put them in the desired format, we will return them as the str with the form we want
    
    
    # Now we introduce the angle one, which allow us to know the angle between the x axis and the vector
    
    def angle(self):
        return math.atan2(self.y, self.x)




if -1 == 1:

    from array import array
    import math
        
        
    class Vector2d:
            
        typecode = 'd' # typecode is a class attribute we’ll use when converting Vector2d instances to/from bytes.
        
                
        def __init__(self, x, y):
            self._x = float(x) # We define the x
            self._y = float(y) # # We define the y
                
        @property
        def x(self): # So we create a mask for the original vector values, now everytime a function operates on self.x, it will be calling this function and receiving the value of self._x, this way self.x cannot be moddified and the vector will be hashable
            return self._x
            
        @property
        def y(self):
            return self._y
                
        def __iter__(self): # __iter__ makes a Vector2d iterable
            return (i for i in (self.x, self.y)) 
                
        def __repr__(self): # Returns an str in they way we want, but the __str__ function has priority if we print
            class_name = type(self).__name__
            return '{}({!r}, {!r})'.format(class_name, *self) 
                
        def __str__(self): # Returns an str in they way we want
            return str(tuple(self))
                
        def __bytes__(self):
            return (bytes([ord(self.typecode)]) # Converts to bytes the unicode of the typecode, which is "d"
            + bytes(array(self.typecode, self))) # Converts to bytes the array formed by the unicode and the coordinates
                
        def __eq__(self, other): # Allows us to make easy comparations
            return tuple(self) == tuple(other) 
                
        def __abs__(self):
            return math.hypot(self.x, self.y) # Calculates the module of the vector
                
        def __bool__(self): 
            return bool(abs(self)) # Returns a True unless the number is 0.0
                
        @classmethod # Class method is modified by the classmethod decorator.
                
        def frombytes(cls, octets): # No self argument; instead, the class itself is passed as cls
                typecode = chr(octets[0]) # Read the typecode from the first byte
                memv = memoryview(octets[1:]).cast(typecode) # Create a memoryview from the octets binary sequence and use the typecode to cast it
                return cls(*memv) # Unpack the memoryview resulting from the cast into the pair of arguments needed for the constructor
                
        def __hash__(self):
            return hash(self.x) ^ hash(self.y) # Returns the XOR of both hashes
                
        
    v1=Vector2d(2, 3)
    print(hash(v1))
    print(set(v1)) # The object is now hashable, so we can set it
    print(v1.__dict__) # Using __slots__ we would prevent the aparition of a __dict__ saving lots of memory
    print(v1._x)
    
    
    
    v1 = Vector2d(1.1, 2.2)
    dumpd = bytes(v1) # Transform v1 to bytes
    print(dumpd)
    print(len(dumpd))
    
    v1.typecode = 'f' # Change the typecode from "d" to "f"
    
    dumpf = bytes(v1) # repeat the process with a different result due to the typecode used, the minimun bytes size of "d" is 8 and for "f" is 4, so the encoded byte string of "f" will be shorter
    print(dumpf)
    print(len(dumpf))
    
    print(Vector2d.typecode) # The general typecode for the class is still "d" the change only applies for v1
    Vector2d.typecode = "f" # This is how we would change the entire class typecode
    
    class Vector2d:
        
        __slots__ = ('_x', '_y') # We can use slots to prevent the creation of a __dict__ and save lots of memory
        typecode = 'd'
    

    



if 1==-1:

    from array import array
    import reprlib
    import math
    
    
    class Vector:
        
            typecode = 'd'
            
            def __init__(self, components):
                self._components = array(self.typecode, components) # Receives the n numbers in an array or a tuple o any kind of list and iters them
            
            def __iter__(self):
                return iter(self._components) # Iters the list
            
            def __repr__(self):
                components = reprlib.repr(self._components) 
                components = components[components.find('['):-1] 
                return 'Vector({})'.format(components)
            
            def __str__(self):
                return str(tuple(self._components))
            
            def __bytes__(self):
                return (bytes([ord(self.typecode)]) +
                        bytes(self._components))
            @classmethod
            def frombytes(cls, octets):
                typecode = chr(octets[0])
                memv = memoryview(octets[1:]).cast(typecode)
                return cls(memv)
    
    
    print(Vector([3.1, 4.2]))
    
    print(Vector((3, 4, 5)))
    
    print(Vector(range(10)))







if 1==-1:
    
    import collections
    
    Card = collections.namedtuple('Card', ['rank', 'suit']) # We create a namedtuple with rank and suit parameters
    
    class FrenchDeck:
        
         ranks = [str(n) for n in range(2, 11)] + list('JQKA') # We define the ranks list
         suits = 'spades diamonds clubs hearts'.split() # And the suit list
         
         def __init__(self):
             self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks] # We create the deck by filling namedtuples with the attributes of each card
         
         def __len__(self):
             return len(self.cards)
         
         def __getitem__(self, position):
             return self.cards[position] # Returns the card in the p position of the array
    
    
    
    
    Deck= FrenchDeck()
    print(len(Deck))
    
    
    
    
# Ok, so the mainly point to use this example is to point out at the fact that using __len__ and __getitem__ in our class, allows us to make it a sequence



if 1==-1:
    
    class Vector:
        
     # many lines omitted
     # ...
     
     def __len__(self):
         return len(self._components)
     
     def __getitem__(self, index):
         return self._components[index]
     
    
    v1 = Vector([3, 4, 5])
    
    len(v1) # 3
    
    v1[0], v1[-1] # (3.0, 5.0). We made it a sequence, and thanks to the __getitem__ we are allowed to fraction it
    
    v7 = Vector(range(7))
    
    v7[1:4] # array('d', [1.0, 2.0, 3.0])




if 1==-1:
    
    class MySeq:
        
        def __getitem__(self, index):  # It basically receives the index
            return index  # And returns it
    
    s = MySeq()
    print(s[1]) # 1. Just an index
    print(s[1:4]) # slice(1, 4, None)
    print(s[1:4:2]) # slice(1, 4, 2) start at 1, stop at 4, setp by 2
    print(s[1:4:2, 7:9]) # (slice(1, 4, 2), slice(7, 9, None)) surprisely it doesn't crash, and returns both slices in a tuple
    
    print(slice) # slice is a built-in type
    print(dir(slice)) # Inspecting a slice we find the data attributes start, stop, and step, and an indices method


    print(slice(None, 10, 2).indices(5)) # [:10:2] is similar to [0:5:2] in this list of len==5 

    print(slice(-3, None, None).indices(5)) # [-3] is similar to [2,5,1]

if 1==-1:
    
    
    from array import array
    import reprlib
    import math
        
        
    class Vector:
            
            typecode = 'd'
            
            def __init__(self, components):
                self._components = array(self.typecode, components) # Receives the n numbers in an array or a tuple o any kind of list and iters them
            
            def __iter__(self):
                return iter(self._components) # Iters the list
            
            def __repr__(self):
                components = reprlib.repr(self._components) 
                components = components[components.find('['):-1] 
                return 'Vector({})'.format(components)
            
            def __str__(self):
                return str(tuple(self._components))
            
            def __bytes__(self):
                return (bytes([ord(self.typecode)]) +
                        bytes(self._components))
            @classmethod
            def frombytes(cls, octets):
                typecode = chr(octets[0])
                memv = memoryview(octets[1:]).cast(typecode)
                return cls(memv)
    
            
            def __len__(self):
                
                return len(self._components)
            
            def __getitem__(self, index):
    
                cls = type(self) 
                if isinstance(index, slice): # Insistance returns True if the object and the type are the same (insistance(5, int)==True)
                    return cls(self._components[index]) 
                elif isinstance(index, int):
                    return self._components[index] 
                else:
                    msg = '{cls.__name__} indices must be integers'
                    raise TypeError(msg.format(cls=cls))
                    
            shortcut_names = 'xyzt'
            
            def __getattr__(self, name):
                cls = type(self) # We get the vector class
                if len(name) == 1: # If it's a 1 character name it can be one of the shortcuts
                    pos = cls.shortcut_names.find(name) # we find the letter's position in the shortcut_names
                    if 0 <= pos < len(self._components): # If the position is in the array
                        return self._components[pos] # Return the number of the vector that has the same position as the letter
                msg = '{.__name__!r} object has no attribute {!r}' 
                raise AttributeError(msg.format(cls, name))
    
            def __setattr__(self, name, value):
                
                 cls = type(self) # We get the class to use it in the future
                 
                 if len(name) == 1: # If the name len==1, ex: v.x
                     if name in cls.shortcut_names: # If the name is in shortcut_names = 'xyzt'
                         error = 'readonly attribute {attr_name!r}' # Write the error
                     elif name.islower():  # If the name is a lower letter (ex: v.j)
                         error = "can't set attributes 'a' to 'z' in {cls_name!r}"  # Write the error
                     else:
                         error = '' # If none of that is fulfilled, the error will be a blank
                         
                     if error: # If there's a non blank text
                         msg = error.format(cls_name=cls.__name__, attr_name=name)
                         raise AttributeError(msg) # Raise the error
                     
                 super().__setattr__(name, value) # Default case: call __setattr__ on superclass for standard behavior
    
    v7 = Vector(range(7))
    print(v7)
    print(v7[-1]) # 6.0. it returns just a numerical value
    print(v7[1:4]) # Vector([1.0, 2.0, 3.0]). It creates a vector to return
    print(v7[-1:]) # Vector([6.0]). It also creates a vector of, because it's a slice of just 1 number, but still a slice
    #print(v7[1,2]) # Error, it activates the else, because this index makes no sense
    
    # And now I want to be able to get the first four coordenates by letter (ex: v.x), we'll use a __getattr_ for that
    
    
    v = Vector(range(5))
    print(v.x) # 0.0 It works
    v.x = 10 # This should raise an error but it doesn't
    print(v.x) # Here we see that the new v.x value is 10
    print(v) # But the vector hasn't changed. What has happenned?
    v.h = 20 # here we have the solution, h is not on the shortcut_names so how can I assign a value to it? Simple, when whe do v.h, we are creating an h attribute with value 20 in the class object, so __getattr__ doesn't get involved in the process
    print(v.h) # And that's why the original array remains intact
    
    
    # To resolve this we have to create a __setattr__ a function that forbides some things in the moment of creating attributes in a class object





if 1==-1:
    
    2 * 3 * 4 * 5 # the result we want: 5! == 120
    
    import functools
    print(functools.reduce(lambda a, b:a*b, range(1,6))) # An easy way to calculate the factorial without importing math
    
    
    n = 0
    
    
    # Now we'll see ways to get the XOR of a numbers chain
    
    for i in range(1, 6): 
        n ^= i # The most classic one, with a for loop
    
    print(n)
    
    import functools
    print(functools.reduce(lambda a, b: a^b, range(6))) # The functools one
    
    import operator
    print(functools.reduce(operator.xor, range(6))) # Another functools but with a XOR function instead of creating it with lambda




if 1==-1:

    from array import array
    import reprlib
    import math
    import functools
    import operator
    
    class Vector:
        
         typecode = 'd'
         # many lines omitted in book listing...
         
         def __eq__(self, other): # We add to the vector class an easy comparation function, it's needed for the hash to work
             return tuple(self) == tuple(other)
         
         def __hash__(self): # Same with the hash
             hashes = (hash(x) for x in self._components) #  first we hash every number on the vector
             return functools.reduce(operator.xor, hashes, 0) # Then we XOR the whole chain as seen before. WARNING: the 0 on the last place is the initializer, and it's good practise to use it to prevent erros
         
         # more lines omitted...
    
    
    # Here we have the same function but with hashes mapped, why would we do that? Because the mapping step produces one hash for each component, and the reduce step aggregates all hashes with the xor operator
    
    
    def __hash__(self):
        
        hashes = map(hash, self._components) # Applies the hash to all the components of the vector
        return functools.reduce(operator.xor, hashes, 0) # And it XORs them
    
    
    # Now let's look at our __eq__ function, it may be effective for short Vectors, but for Vector instances that may have thousands of components, it’s very inefficient.
    
    
    def __eq__(self, other):
        
         if len(self) != len(other): # If lens doesn't match they cannot be the same Vector, so it returns False
             return False
         for a, b in zip(self, other): # Let's look at the concept of zip, it produces a generator of tuples made from the items in each iterable argument, we'll look deeper in the next lines
             if a != b: # If they don't match it returns False
                 return False
         return True
    
    
    # This example looks much better and efficient, but we can make it in one line
    
    
    def __eq__(self, other):
        return len(self) == len(other) and all(a == b for a, b in zip(self, other)) # It's harder to read, but more compact, and with a medium python level completely understandable





if 1==-1:

    # In a foor loop, the zip built-in makes it easy to iterate in parallel over two or more iterables by returning tuples that you can unpack into variables, one for each item in the parallel inputs.
    
    print(zip(range(3), 'ABC')) # Zip returns a generator that produces tuples on demand
    
    print(list(zip(range(3), 'ABC'))) # We receive a paired list from both list from the zip
    
    print(list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3]))) # Same, but take a look at the 3.3 it doesn't appear because one or more other lists have gone out of range
    
    from itertools import zip_longest # The itertools.zip_longest function behaves differently: it uses an optional fillvalue (None by default)to complete missing valuesso it can generate tuples until the last iterable is exhausted.
    print(list(zip_longest(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3], fillvalue=-1)))