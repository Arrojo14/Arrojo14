# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 11:35:36 2021

@author: larro
"""


from array import array
import math
import reprlib



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




# we'll implement some new Unary operator methods on the vector class 


        def __abs__(self):
            return math.sqrt(sum(x * x for x in self))
        
        def __neg__(self):
            return Vector(-x for x in self)  # Returns a vector with all the coordinates into the other sign
        
        def __pos__(self):
            return Vector(self) # Returns a new vector with every component of self as it was

# We haven't implemented __invert__, so if someone tries ~v on a vector, it will crash
            
            
            
# Could you imagine x == +x being False? Well, ther're two cases where that happens.
    

        
if 1==-1:
         
    import decimal
    
    ctx = decimal.getcontext() # Get a reference to the current global arithmetic context. 
    ctx.prec = 40  # Set the precision to 40
    one_third = decimal.Decimal('1') / decimal.Decimal('3') # 1/3 using the context precision
    print(one_third) # 40 fucking decimals
    
    print(one_third == +one_third ) # True as expected
    
    ctx.prec = 28   # Lower the precision to the default, 28
    print(one_third == +one_third) # Now it's false, but why?  it's because using the + makes Python to produce a new Decimal instance reconsiderating the decimal context, whose prec is now 28
    
    print(+one_third) # 28 decimals as we specified on line 118



            
# Let's see the other case


if 1==-1:
    
    from collections import Counter
    
    ct = Counter('abracadabra') # A counter returns how many times a word is cloned on an str
    print(ct)
    
    ct['r'] = -3
    ct['d'] = 0
    
    print(ct) # The counter returns the values with the changes made
    
    print(+ct) # But once we use +ct, the counter updates and detects that values 0 and -3 are impossible, so it deletes them

        
            
            
# Back to vectors and unitary operators


# We want the vectors to be able to be added to another vector

import itertools

def add(self, other):
    return Vector([i+j for i, j in itertools.zip_longest(self, other, fillvalue= 0.0)]) # Take a look at the fillvalue, if we didn't use it, the program would crash because the original fillvalue is None and you can't add None


Vector.__add__ = add
            
if 1==-1:
    
    v1 = Vector([3, 4, 5])
    v2 = Vector([6, 7, 8])
    v3 = Vector([1, 2])
    print(v1 + v2)
    print(v1 + v2 == Vector([3+6, 4+7, 5+8]))
    print(v1 + v3)
                
                
    # It supports non vectors too
            
    v1 = Vector([3, 4, 5])
    print(v1 + (10, 20, 30))
    
    # But what happens if we put the non vector in the left of the add?
    
                
    v1 = Vector([3, 4, 5])
    (10, 20, 30) + v1 # can only concatenate tuple (not "Vector") to tuple, because it no longer goes to the Vector.__add__ method it goes to the tuple __add__
                
            
            
# On a (a+b) python will look for an a.__add__ method, if it exists and result is implemented, it will return a result, if not it will use the b.__add__ and follow the same process, but if b.__add__ doesn't exist also or hasn't got the result implemented, it will raise TypeError
            
            
            
            
# The __radd__ method is called the “reflected” or “reversed” version of __add__. They are called on the righthand operand          
          
            
    
          
def radd(self, other):
    return self + other # __radd__ just delegates to __add__.

Vector.__radd__= radd       
          
            

            
# We can modify __add__ to just return NotImplemented

def add(self, other):
    try:
        return Vector([i+j for i, j in itertools.zip_longest(self, other, fillvalue= 0.0)]) # Take a look at the fillvalue, if we didn't use it, the program would crash because the original fillvalue is None and you can't add None
    except TypeError:
        return NotImplemented        
          
            
def radd(self, other):
    return self + other       
          

def mul(self, n):
    return Vector(i*n for i in self)

def rmul(self, scalar):
    return self * scalar



Vector.__add__= add
Vector.__radd__= radd
Vector.__mul__= mul
Vector.__rmul__= rmul
            

if 1==-1:
    v1 = Vector([3, 4, 5])
    print(v1*10)
          
            
# We can also modify mul to not explode when trying to multiplicate something

import numbers
            
def mul(self, n):
    if isinstance(n, numbers.Real):
        return Vector(i*n for i in self)
    else:
        return NotImplemented


def rmul(self, scalar):
    return self * scalar  
            
            
Vector.__mul__= mul
Vector.__rmul__= rmul
            

# The use of the @ infix operator

def matmul(self, other):
    
    try:
        return sum(a * b for a, b in zip(self, other))
    
    except TypeError:
        return NotImplemented
    
def rmatmul(self, other):
    return self @ other


Vector.__matmul__= matmul
Vector.__rmatmul__= rmatmul


if 1==-1:
    
    va = Vector([1, 2, 3])
    vz = Vector([5, 6, 7])
    print(va @ vz) #  1*5 + 2*6 + 3*7 = 38
    print([10, 20, 30] @ vz)

            

def eq(self, other): # Much different to the books one but way more optimized
    
    if len(self)!=len(other):
        return False
    else:
        for i, j in zip(self, other):
            if i!=j:
                return False
        return True
    
            
Vector.__eq__ = eq


if 1==-1:
    
    va = Vector([1.0, 2.0, 3.0]) 
    vb = Vector(range(1, 4))
    print(va == vb)
    t3 = (1, 2, 3) # This method compares Vectors to tuples, only minding the numbers in both, this is not what we want, so we'll reformulate this
    print(va == t3)

            
          
            
def eq2(self, other): # Much different to the books one but way more optimized
    
    if not len(self)==len(other) or not isinstance(other, Vector): # Also checks that type is Vector
        return NotImplemented # We change the False for a NotImplemented
    else:
        for i, j in zip(self, other):
            if i!=j:
                return NotImplemented
        return True 
            
          
            
Vector.__eq__ = eq2     
            


if 1==-1:
          
    va = Vector([1.0, 2.0, 3.0]) 
    vb = Vector(range(1, 4))
    print(va == vb)
    t3 = (1, 2, 3) 
    print(va == t3) # Now we receive False because a tuple is not a Vector    
    vc= Vector([1,2])
    print(va==vc) # Also returns False when lens doesn't match
        
            
# Now, what about the !=

if 1==-1:
    va = Vector([1.0, 2.0, 3.0]) 
    vb = Vector(range(1, 4))
    va != vb # False
    va != (1, 2, 3) # True

# What we haven't implemented __ne__ then how is it working?
# Because the fallback behavior of the __ne__ inherited from object suits us: when __eq__ is defined and does not return NotImplemented, __ne__ returns that result negated


# How does __ne__ works:
    

def __ne__(self, other):
    eq_result = self == other
    if eq_result is NotImplemented:
        return NotImplemented
    
    
if 1==-1:
    
    v1 = Vector([1, 2, 3]) # We create a Vector object
    v1_alias = v1 # We create v1_alias which points at Vector([1, 2, 3])
    print(id(v1)) # 2073974085856
    
    v1 += Vector([4, 5, 6]) # We add v1 to another Vector
    print(v1) # 
    print(id(v1)) # Id has changed, a new Vector has been created
    
    print(v1_alias) # (1.0, 2.0, 3.0) It hasn't changed, because the object that is pointing at hasn't also changed
    v1 *= 11 
    print(v1) # (55.0, 77.0, 99.0) as expected
    print(id(v1)) #4302858336 a different one than before, a new object has been created again




# If a class does not implement the in-place operator, the augmented assignment operators are just syntactic sugar: a += b is evaluated exactly as a = a + b. That’s the expected behavior for immutable types, and if you have __add__ then += will work with no additional code

# However, if you do implement an in-place operator method such as __iadd__, that method is called to compute the result of a += b


class AddableBingoCage(): 
    
    def __add__(self, other):
        
        if isinstance(other, AddableBingoCage): # Our __add__ will only work with an instance of AddableBingoCage as the second operand
            return AddableBingoCage(self.inspect() + other.inspect()) # retrieve items from other
        else:
            return NotImplemented
        
        
    def __iadd__(self, other):
        
        if isinstance(other, AddableBingoCage): 
            other_iterable = other.inspect()  # Retrieve items from other
        else:
            try:
                other_iterable = iter(other) # If that fails, raise an exception explaining what the user should do
            except TypeError: 
                self_cls = type(self).__name__
                msg = "right operand in += must be {!r} or an iterable"
                raise TypeError(msg.format(self_cls))
        self.load(other_iterable) # Very important: augmented assignment special methods must return self.
        return self



# Let's lear about iterables 


import re
import reprlib
RE_WORD = re.compile('\w+')

class Sentence:
    
     def __init__(self, text):
         self.text = text
         self.words = RE_WORD.findall(text) # The findall expresion will create an array with every word on the sentence escaping from special characters
         
     def __getitem__(self, index):
         return self.words[index] # Returns the words in order depending on the index
    
     def __len__(self): 
         return len(self.words) # returns number of words
     
     def __repr__(self):
         return 'Sentence(%s)' % reprlib.repr(self.text) # returns the correct sentence


if 1==-1:
    f1=Sentence("Hoy no $a hay futbol")
    print(len(f1))
    s = Sentence('"The time has come," the Walrus said,')
    for w in s: # We can only do this thanks to the getitem method that makes the object iterable
        print(w)


# The iter built-in function:
    
# 1. Checks whether the object implements __iter__, and calls that to obtain an iterator.
# 2. If __iter__ is not implemented, but __getitem__ is implemented, Python creates an iterator that attempts to fetch items in order, starting from index 0 (zero).
# 3. If that fails, Python raises TypeError, usually saying “C object is not iterable,” where C is the class of the target object.



# An str is not iterable by itself but it is using a for loop or creating our "handmade" iterator to show how does it work

if 1==-1:
    s = 'ABC'
    it = iter(s) # It will iter the str making it an iterable
    
    while True:
        
        try:
            print(next(it)) # prints the next variable of the iterator, the first one if it's the first time
        except StopIteration: # stops when there's no more words
            del it # deletes the iteratir
            break

if 1==-1:
    
    from collections import abc
    
    class Iterator(abc.Iterable): # We create a class that is itself an Iterable
        
         __slots__ = ()
         @abc.abstractmethod
         def __next__(self):
             'Return the next item from the iterator. When exhausted, raise StopIteration'
             raise StopIteration
             
         def __iter__(self):
             return self # Just return the object, is an iterable itself
         
         @classmethod
         def __subclasshook__(cls, C):
             if cls is Iterator:
                 if (any("__next__" in B.__dict__ for B in C.__mro__) and any("__iter__" in B.__dict__ for B in C.__mro__)):
        
                     return True
                 return NotImplemented




class Sentence:
    
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    def __iter__(self): # We redifine the Sentence class but instead of iterating the sentence by the __getitem__ method, we create an __iter__
         return SentenceIterator(self.words) 
    
    
class SentenceIterator:
    
    def __init__(self, words):
        self.words = words
        self.index = 0 
        
    def __next__(self):
        try:
            word = self.words[self.index] # It basically adds the word "qualifying" for each word of words and returns it till there's no more and the except is activated
        except IndexError:
            raise StopIteration() 
        self.index += 1 
        return word
    
    def __iter__(self): 
        return self




# now let's talk about generators, for that we have to add some changes to the Sentence class


class Sentence:
    
     def __init__(self, text):
         self.text = text
         self.words = RE_WORD.findall(text) # The findall expresion will create an array with every word on the sentence escaping from special characters
         
     
     def __repr__(self):
         return 'Sentence(%s)' % reprlib.repr(self.text) # returns the correct sentence

     def __iter__(self):
         for w in self.words:
             yield w # Yield turns the function into a generator
         return

if 1==-1:
    
    f1=Sentence("Hoy no $a hay futbol")
    it=iter(f1)
    print(next(it)) # As a the iterator it makes the Sentence an iterable, we're able to use the next() command or the for loop to obtain the words one by one


# Here is a simple example of a generator

def gen_123(): # The moment we include yield(item) in a function, it becomes a generator
    yield 1 
    yield 2
    yield 3


if 1==-1:
    print(gen_123)
    for i in gen_123(): 
        print(i)
        
    g=gen_123()
    while True:
        print(next(g)) # When the body of the function completes, the generator object raises a StopIteration
        
    


def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')

    # yields 'A' and 'B', and that's the variables that the generator will give as iterables

if 1==-1:
    for c in gen_AB():
        print('-->', c)
        
        #start
        #--> A
        #continue
        #--> B
        #end.
        
        # But why do start, continue and end take part of the for loop?
        # Because the actions on the generator take part after/before the yield is called, for example the start will be printed just before the first next(generator) is called, and continue after it



class Sentence:
    
    def __init__(self, text):
        self.text = text 
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        for match in RE_WORD.finditer(self.text): # finditer builds an iterator over the matches of RE_WORD on self.text, yielding MatchObject instances
            yield match.group() # match.group() extracts the actual matched text from the MatchObject instance.



if 1==-1:
    res1 = [x*3 for x in gen_AB()] # Creates a list with 3 times each yield item of the generator, ("A" and "B)
    print(type(res1))
    for i in res1:
        print('-->', i) #prints res1
        
    res2 = (x*3 for x in gen_AB()) # The generator expression returns res2. The call to gen_AB() is made, but that call returns a generator, which is not consumed here.
    
    
    for i in res2:
        print('-->', i) #prints res2, but now the start,cont.... msgs don't appear until the for loop print, why?






class Sentence:
    
    def __init__(self, text):
        self.text = text
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text)) # the __iter__ method, which here is not a generator function (it has no yield) but uses a generator expression to build a generator and then returns it
    




class ArithmeticProgression:
    
    def __init__(self, begin, step, end=None): 
        self.begin = begin
        self.step = step
        self.end = end # None -> "infinite" series
    
    def __iter__(self):
        result = type(self.begin + self.step)(self.begin) # This basically takes the type of the add of begin and step and converts the begin to that type 
        forever = self.end is None 
        index = 0
        while forever or result < self.end: 
            yield result # The current result is produced and the __iter__ turns into a generator
            index += 1
            result = self.begin + self.step * index # The next potentialresult is calculated. It may never be yielded, because the while loop may terminate




if 1==-1:
    
    ap = ArithmeticProgression(0, 2, 17)
    it=iter(ap) # There're some ways of activating the iter function, creating a list, doing a for loop or iter the self.class()
    print(next(it)) 



# here we have a more optimized model, consists of a function that returns a generator

def aritprog_gen(begin, step, end=None):
    
     result = type(begin + step)(begin)
     forever = end is None
     index=0
     while forever or result < end:
         yield result
         index += 1
         result = begin + step * index


if 1==-1:
    ar=aritprog_gen(1,3,20)
    while True:
        try:
            print(next(ar), end=" ")
        except: break




# Arithmetic Progression with itertools

# The itertools module in Python 3.4 has 19 generator functions that can be combined in a variety of interesting ways.



import itertools
gen = itertools.count(1, .5)


if 1==-1:
    print(next(gen))
    # 1 beginning
    print(next(gen))
    # 1,5 begin + step
    print(next(gen))
    # 2 begin + step*2
    print(next(gen))
    # 2,5 begin + step*3


if 1==-1:
    gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5)) # the itertools.takewhile function produces a generator that consumes another generator and stops when a given predicate evaluates to False. So we can combine the two.
    print(list(gen))
    
    
    
def vowel(c):
    return c.lower() in 'aeiou' # Returns True if the letter is a vocal, else: False

    
# Here I have two versions of how we could use the Vowel generator
 
if 1==-1:
    
   print([i for i in 'Aardvark' if vowel(i)])
   print([i for i in 'Aardvark' if not vowel(i)])
   
   print(list(filter(vowel, 'Aardvark')))
    


# Itertools guide

#  import itertools

# itertools.tool(statement, iterable)

# itertools.filterfalse()   # Allows us to keep the characters of the iterable that return false under a statement
# itertools.dropwhile()   # Starts with the n character when it returns False and continues till the list ends
# itertools.takewhile()   # Stops when some character returns false under the statement


# itertools.tool(iterable, slice)
#  itertools.islice() # Allows us to slice the iterable as we want
    


# Generator function examples
    
if 1==-1:
    
    print(list(itertools.chain('ABC', range(2)))) # itertools.chain allows us to join two iterables
    
    print(list(itertools.chain(enumerate('ABC')))) # chain does nothing useful when called with a single iterable
    
    print(list(itertools.chain.from_iterable(enumerate('ABC')))) # But chain.from_iterable takes each item from the iterable, and chains them in sequence, as long as each item is itself iterable
    
    print(list(zip('ABC', range(5)))) # Not even gonna explain
    
    print(list(zip('ABC', range(5), [10, 20, 30, 40]))) # Again, this is basic
    
    print(list(itertools.zip_longest('ABC', range(5)))) # basic
    
    print(list(itertools.zip_longest('ABC', range(5), fillvalue='?'))) # basic
        
        
    
    
# itertools.product(iterable, iterable)
    
    
if 1==-1:
    
    print(list(itertools.product('ABC', range(2)))) # Returns like a zip but with every character of the first list with each character of the second list
    
    suits = 'spades hearts diamonds clubs'.split()
    
    print(list(itertools.product('AK', suits))) # same as above
    
    print(list(itertools.product('ABC'))) # With a single iterable, product is not very usefull
    
    print(list(itertools.product('ABC', repeat=2))) # Acts as if the second list of the product was similar to the first one
    
    print(list(itertools.product(range(2), repeat=3))) # Same but with three
        
    

if 1==-1:
    
    import operator
    
    ct = itertools.count() # Starts an iterator that returns n+1 starting with n=0 everytime is called
    print(next(ct)) # 0
    
    print(next(ct), next(ct), next(ct)) # 1 2 3
    
    print(list(itertools.islice(itertools.count(1, .3), 3))) # With itertools.islice(it, 3) we get the first 3 numbers of itertools.count(1, .3) that are 1,1.3 and 1.6
    
    cy = itertools.cycle('ABC') # Build a cycle generator from 'ABC' and fetch its first item, 'A'.
    print(next(cy))
    
    print(list(itertools.islice(cy, 7))) # A list can only be built if limited by islice; the next seven items are retrieved here
    
    rp = itertools.repeat(7) # Build a repeat generator that will yield the number 7 foreve
    print(next(rp), next(rp))
    
    print(list(itertools.repeat(8, 4))) # Build a repeat generator that will yield the number 8 for 4 times
    
    print(list(map(operator.mul, range(11), itertools.repeat(5)))) # A common use of repeat: providing a fixed argument in map; here it provides the 5 multiplier
        
    
    
if 1==-1: 
    
    # itertools.combinations(iterable, iterable) / itertools.permutations(iterable, iterable)


    print(list(itertools.combinations('ABC', 2))) # All possible combinations of len==2 with "A" "B" and "C"
    
    print(list(itertools.combinations_with_replacement('ABC', 2))) # All combinations of len()==2 from the items in 'ABC', including combinations with repeated items.
    
    print(list(itertools.permutations('ABC', 2))) # Same as 1 but with order included on the posibilities of the combination
    
    print(list(itertools.product('ABC', repeat=2))) # Been before
        
    
 
    
if 1==-1:
    
    # itertools.grouby(iterable, key)
    
    print(list(itertools.groupby('LLLLAAGGG'))) # So this yields tuples with 2 objects, the character of the group and the group, it groups the following characters/word that share the groupby key, in this case being the same character
    
    for letter, group in itertools.groupby('LLLLAAGGG'):
        print(letter, "-->", list(group))
    
    animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin', 'shark', 'lion']
    x=sorted(animals, key=len)
    for letter, group in itertools.groupby(x, len): # Instead of the same character, we set the group indices as the len of the words in the group
        print(letter,"---->", list(group))
     
    
 
if 1==-1:
    
    # itertools.tee(iterable, n)
     
    print(list(itertools.tee('ABC'))) #  itertools.tee yields n (2 by default) generators, each yielding every item of the input generator
     
    g1,g2,g3 = list(itertools.tee('ABC',3))
    print(next(g1))
    print(next(g2))
    print(next(g3))
     
    for i in zip(g1,g2,g3):
        print("x3 ----->", i)
 
    
 
if 1==-1:
    
    
    def chain(*iterables):
        for it in iterables:
            for i in it:
                yield i # Yields i for every character of every iterable obtained by the function, making the function a generator that will return the characters in order as a chain function
    
    s = 'ABC'
    t = tuple(range(3))
    print(list(chain(s, t)))
    
    # But can we change the function syntax to make it shorter? Yes
    
    def chain(*iterables):
        for i in iterables:
            yield from i # yield from i replaces the inner for loop completely, besides replacing a loop, yield from creates a channel connecting the inner generator directly to the client of the outer generator. This channel becomes really im‐ portant when generators are used as coroutines and not only produce but also consume values from the client code
    
    print(list(chain(s, t)))
 

if 1==-1:
    
    
    # All and any
    
     
    # all() Returns True if all items in it are truthy, otherwise False; all([]) returns True
    
    print(all([1, 0, 3]))
    
    print(all([1, 2, 3]))
    
    print(all([]))
    
    
    # any() Returns True if any item in it is truthy, otherwise False; any([]) returns False
    
    print(any([1, 2, 3]))
    
    print(any([0, 0, 0]))
    
    print(any([]))