# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 18:25:52 2021

@author: larro
"""

if 1==-1:
    
    def factorial(n): # I made a different model than the book one, but I think mine is way more understandable and must be close in terms of optimization
        '''RETURNS n!'''
        x=n
        while x>1:
            x=x-1
            n = x*n
        return n
    
    print(factorial(42))
    print(factorial.__doc__) # The doc attribute returns the function's description if there's one, if not, returns None
    
    


if 1==-1: # map function applies a function to a whole list/tuple/array/...
    
    def factorial(n):
            '''RETURNS n!'''
            x=n
            while x>1:
                x=x-1
                n = x*n
            return n
    
    ft=factorial
    
    print(ft(5))
    
    print(list(map(ft,(n for n in range(11)))))




if 1==-1: # The whole purpose of this code is to show that you can use a function as a key to sort a list. If you need to call a function with a dynamic set of arguments, you can just write fn(*args, **keywords) instead of apply(fn, args, kwargs).
    
    def reverse(word):
        return word[::-1]
    
    
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(sorted(fruits, key=reverse))



if 1==-1:
    
        def factorial(n):
            '''RETURNS n!'''
            x=n
            while x>1:
                x=x-1
                n = x*n
            return n
        
        print(list(map(factorial,range(6))))
        print(list(factorial(n) for n in range(6)))
        print(list(map(factorial, filter(lambda n: n % 2, range(6))))) # List of factorials of odd numbers up to 5!, using both map and filter
        print(list(factorial(n) for n in range(6) if n%2)) # Same as before but without map
        
        
if 1==-1:
    
    from functools import reduce # Not the book's way of doing it but a more practical one. No need to import add, the reduce function itself gives you utilities to add the numbers of a list.
    print(reduce(lambda a, b:a+b,range(100)))    
        

if 1==-1:
    
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(sorted(fruits,key= lambda word: word[::-1])) 


# The lambda function has two ways of use:
# 1 variable: lambda x: (changes to x)
# 2 or more variable (usually lists): lambda a, (relation between a and b)


if 1==-1:
    
    import random
    
    
    class BingoCage:
        
     def __init__(self, items):
         self.items = list(items) # Bingo's items will be the list's items
         random.shuffle(self.items) # Random sort
    
     def pick(self):
         try:
             return self.items.pop() # Pick the last item of the randomly sorted list
         except IndexError:
             raise LookupError('pick from empty BingoCage') 
             
     def __call__(self): 
         return self.pick() # I will execute pick everytime the function is called
     
        
    bingo = BingoCage(range(3))
    print(bingo.pick())
    print(bingo())



if 1==-1:
    
    def factorial(n):
                '''RETURNS n!'''
                x=n
                while x>1:
                    x=x-1
                    n = x*n
                return n
    
    print(dir(factorial)) # Shows the possible attributes of a class/function



if 1==-1:
    
    class C: pass 
    obj = C() 
    def func(): pass 
    print(sorted(set(dir(func)) - set(dir(obj)))) # Using set difference, generate a sorted list of the attributesthat exist in a function but not in an instance of a bare class
    
    
    
if 1==-1: 
    
    def tag(name, *content, cls=None, **attrs):
     """Generate one or more HTML tags"""
     if cls is not None:
         attrs['class'] = cls
     if attrs:
         attr_str = ''.join(' %s="%s"' % (attr, value)
                            for attr, value
                            in sorted(attrs.items()))
     else:
         attr_str = ''
     if content:
         return '\n'.join('<%s%s>%s</%s>' %
                          (name, attr_str, c, name) for c in content)
     else:
         return '<%s%s />' % (name, attr_str)
    
    
    print(tag({"class":2}))


# Here should be the Bobo script, an HTTP micro framework in library form. In the example you made a simple code which made Bobo say f"Hello {person}" to anyone who would visit http://localhost:8080/
# But it would fail due to the fact that the name hadn't been introduced. But if you entered into  http://localhost:8080/?person=Arrojo this error wouldn't ocurr, in fact you'd receive "Hello Arrojo" as the user has been introduced.
# The example is not here because the library installation didn't work and I don't wanna waste time


if 1==-1:
    
    def clip(text, max_len=80): # Within a function object, the __defaults__ attribute holds a tuple with the default values of positional and keyword arguments. The defaults for keyword-only arguments appear in __kwdefaults__. The names of the arguments, however, are found within the __code__ attribute, which is a reference to a code object with many attributes of its own
     """Return text clipped at the last space before or after max_len
     """
     
     end = None
     if len(text) > max_len: # If text's lenght is longer than max_len
         space_before = text.rfind(' ', 0, max_len) # Finds the last space before the text
         
         if space_before >= 0:
             end = space_before
         else:
                space_after = text.rfind(' ', max_len) #FInds the first space after the text
                if space_after >= 0:
                    end = space_after
                    
     if end is None: # no spaces were found
         end = len(text)
     return text[:end].rstrip()
    
    
    
    print(clip.__defaults__) # Default values on the function (max_len in this case)
    print(clip.__code__.co_varnames) # Name of variables that take part in the function
    print(clip.__code__.co_argcount) # Number of arguments




if 1==-1:
    
    def clip(text, max_len=80): # Within a function object, the __defaults__ attribute holds a tuple with the default values of positional and keyword arguments. The defaults for keyword-only arguments appear in __kwdefaults__. The names of the arguments, however, are found within the __code__ attribute, which is a reference to a code object with many attributes of its own
         """Return text clipped at the last space before or after max_len
         """
         
         end = None
         if len(text) > max_len: # If text's lenght is longer than max_len
             space_before = text.rfind(' ', 0, max_len) # Finds the last space before the text
             
             if space_before >= 0:
                 end = space_before
             else:
                    space_after = text.rfind(' ', max_len) #Finds the first space after the text
                    if space_after >= 0:
                        end = space_after
                        
         if end is None: # no spaces were found
             end = len(text)
         return text[:end].rstrip()
    
    from inspect import signature
    
    sig = signature(clip)
    print(sig) # Parameters on clip
    
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default) # kind, name and description of parameters in clip




if 1==-1:

    def tag(name, *content, cls=None, **attrs):
         """Generate one or more HTML tags"""
         if cls is not None:
             attrs['class'] = cls
         if attrs:
             attr_str = ''.join(' %s="%s"' % (attr, value)
                                for attr, value
                                in sorted(attrs.items()))
         else:
             attr_str = ''
         if content:
             return '\n'.join('<%s%s>%s</%s>' %
                              (name, attr_str, c, name) for c in content)
         else:
             return '<%s%s />' % (name, attr_str)
        
        
    
    import inspect
    sig = inspect.signature(tag) 
    print(sig) # Get the signature from tag function
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
    bound_args = sig.bind(**my_tag) # Pass a dict of arguments to .bind()
    print(bound_args)
     
    for name, value in bound_args.arguments.items(): # Iterate over the items in bound_args.arguments, which is an OrderedDict, to display the names and values of the arguments
        print(name, '=', value)
    
    name = img
    cls = framed
    attrs = {'title': 'Sunset Boulevard', 'src': 'sunset.jpg'}
    del my_tag['name'] # Remove the mandatory argument name from my_tag
    bound_args = sig.bind(**my_tag) # Calling sig.bind(**my_tag) raises a TypeError complaining of the missing name parameter.
    



if 1==-1:
    
    def clip(text:str, max_len:'int > 0'=80) -> str: 
     """Return text clipped at the last space before or after max_len
     """
     end = None
     if len(text) > max_len:
         space_before = text.rfind(' ', 0, max_len)
         if space_before >= 0:
             end = space_before
         else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
     if end is None: # no spaces were found
         end = len(text)
     return text[:end].rstrip()
    
    
    print(clip.__annotations__) # Print the annotations made on the function parameters



if 1==-1:
    def clip(text:str, max_len:'int > 0'=80) -> str: 
         """Return text clipped at the last space before or after max_len
         """
         end = None
         if len(text) > max_len:
             space_before = text.rfind(' ', 0, max_len)
             if space_before >= 0:
                 end = space_before
             else:
                space_after = text.rfind(' ', max_len)
                if space_after >= 0:
                    end = space_after
         if end is None: # no spaces were found
             end = len(text)
         return text[:end].rstrip()
     
    
    from inspect import signature
    
    sig = signature(clip)
    print(sig.return_annotation) # Returns the annotations made on the function parameters
    
    for param in sig.parameters.values():
        note = repr(param.annotation).ljust(13)
        print(note, ':', param.name, '=', param.default)


if 1==-1:
    
    from functools import reduce
    
    def fact(n):
        return reduce(lambda a, b:a*b, range(1,n+1))



if 1==-1:
    metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
    ]
    
    from operator import itemgetter
    
    for city in sorted(metro_data, key= itemgetter(1)): # Thanks to the itemgetter, we can sort the array by any of the arguments give, in this case, the [1] position, the initials of the counntry.
        print(city)
    
    for city in metro_data: # We can use the itemgetter to print only specific things on the array by indicating their position in order 
        print((itemgetter(1,0))(city))
        
    for city, country, nm, (n1, n2) in metro_data: # Proof that the itemgetter is a good helper but not strictly necessary
        print("(%r, %r)" % (country, city))



# A sibling of itemgetter is attrgetter, which creates functions to extract object at‐ tributes by name. If you pass attrgetter several attribute names as arguments, it also returns a tuple of values. In addition, if any argument name contains a . (dot), attrgetter navigates through nested objects to retrieve the attribute.
# The example will be large because we need to build an structure tu fully show what does attrgetter do

if 1==-1:
    from collections import namedtuple
    
    metro_data = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
        ]
    
    Metropolis=namedtuple("Metropolis",["name", "cc", "pop", "coord"])
    LatLong=namedtuple("LatLong",["lat","long"])
    
    
    
    metro_areas= [Metropolis(name, cc, pop, LatLong(lat, long)) for name, cc, pop, (lat, long) in metro_data]
    
    print(metro_areas[0].coord.long)
    
    # OK, so till now we've created a list made of two namedtuples (Metropolis and LatLong), so now we can check the real use of attrgetter
    
    from operator import attrgetter, itemgetter
    
    for city in sorted(metro_areas, key=attrgetter('coord.lat')): # As we can see, the main difference between attrgetter and itemgetter is that with itemgetter we can only choose by items position, but with attrgetter we can use names, but tbh both can do the same work and I see the itemgetter a little bit more practical.
        print((attrgetter('name', 'coord.lat'))(city))
    
    for city in sorted(metro_data, key=((itemgetter(3)))): # In this case we cannot do the same as with attrgetter.
        print(itemgetter(0,3)(city))




if 1==-1:   # Methodcaller its some‐what similar to attrgetter and itemgetter in that it creates a function on the fly. The function it creates calls a method by name on the object given as argument.
    
    from operator import methodcaller
    s = 'The time has come'
    upcase = methodcaller('upper')
    print(upcase(s)) # Calls upper method on s given as argument
    
    hiphenate = methodcaller('replace', ' ', '-')
    print(hiphenate(s)) # Calls hiphenate method on s given as argument



if 1==-1:
    
    from operator import mul
    from functools import partial # So basically what partial does is similar to methodcaller but with methods that need 2 arguments as mul(a, b), the use would be: partial(method, 1st value)
    
    mult5 = partial(mul, 5)
    
    print(mult5(6))
    
    print(list(mult5(n) for n in range(11))) # We can use it to print the 5 times table for example




if 1==-1:
    
    import unicodedata, functools
    
    
    nfc= functools.partial(unicodedata.normalize, "NFC") # We create a partial to normalize with NFC method
    
    s1 = 'café'
    s2 = 'cafe\u0301'
    
    print(s1==s2) # It's false because the code hasn't been normalized yet, if the partial works, next one should be True
    print(nfc(s1)==nfc(s2)) # It's True, so it works perfectly.