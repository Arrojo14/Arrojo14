# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 17:50:11 2021

@author: larro
"""


if 1==-1:
    
    def deco(func):
        
        def inner():
            print('running inner()')
            
        return inner 
    
    @deco
    def target():
        print('running target()')
    
    target()



if 1==-1: # With the decorator we're able to call a decorator function with another one as argument, while having other arguments on the background.
   
    registry = []
    
    def register(func):
        def sc():
            print('running register(%s)' % func) 
            registry.append(func)
            func()
        return sc 
    
    
    @register 
    def f1():
     print('running f1()')
    
    @register 
    def f2():
     print('running f2()')
    
    def f3(): 
     print('running f3()')
     
     
    
    def main():
        print('running main()')
        print('registry ->', registry)
        f1()
        f2()
        f3()
    
    if __name__=='__main__':
     print("YES")
     main()
    
    print(registry)
    
    
if 1==-1:
    
    promos = [] 
    def promotion(promo_func): 
     promos.append(promo_func)
     return promo_func
    
    @promotion 
    def fidelity(order):
     return order.total() * .05 if order.customer.fidelity >= 1000 else 0
    
    
    @promotion
    def bulk_item(order):
     """10% discount for each LineItem with 20 or more units"""
     discount = 0
     for item in order.cart:
         if item.quantity >= 20:
             discount += item.total() * .1
     return discount
    
    
    @promotion
    def large_order(order):
     """7% discount for orders with 10 or more distinct items"""
     distinct_items = {item.product for item in order.cart}
     if len(distinct_items) >= 10:
         return order.total() * .07
     return 0
    
    
    def best_promo(order): 
     """Select best discount available
     """
     return max(promo(order) for promo in promos)
  

    
if 1==-1: # This is a little weird if it's the 1st time you've seen it, in theory this should print 6 and 3 instead of 6 and error: 
    
    def printt(a):
        
        print(a)
        print(b)
        b=7
        return None
    
        
    b=3
    printt(6)
    

# This happens because we define b inside the function but after the print(b), so python detects b as a local argument and ignores the global one. But the local b comes after the print, so it isn't assigned yet
# We can solve this by indicating python to take the global value of b if it hasn't been assigned yet on the function
    
if 1==-1:
    
    def printt(a):
        
        global b # We tell python to take the globa value of b
        print(a)
        print(b) # It uses the global value because it hasn't been defined yet on the function
        b=7 # We define an specific value inside the function
        print(b) # It uses the value we just defined
        return None
    
        
    b=3
    printt(6)
    
    
    
if 1==-1:  
    class Averager():
        
     def __init__(self):
         self.series = []
         
     def __call__(self, nmb):
         self.series.append(nmb)
         x=0
         for n in self.series:
             x+=n
         return (x/len(self.series))
             
    
    avg = Averager()
    print(avg(3))
    
    
 
if 1==-1: # Basically with avg=elarrai() we make python to exevcute only the subfunction "averager" making the array of "elarrai" exist all the time. This is not a good practise, so the example is mostly unusable
    def elarrai():
        por_que=[]
        
        def averager(nmb):
            por_que.append(nmb)
            return (sum(por_que)/len(por_que))
        
        return averager
    
    avg=elarrai()
    print(avg(3))
    print(avg(5))
    print(avg(7))



if 1==-1:
    
    def make_averager():
         count = 0
         total = 0
         
         def averager(new_value):
             global count, total
             count += 1
             total += new_value
             return total / count
         
         return averager





    x="hol QUE Tal".split(" ")
    y=[]
    y.append((x.lower for x in x))
    print(y)




if 1==-1: # Basically this code is all about in showing us that keywords are compatible with decorators, and showing the way we can combine them in. If we wanted to add a third argument as a list, we would need a wrapper inside the second func.
    registry = set()
    
    def register(active=True): 
        def decorate(func): 
            print('running register(active=%s)->decorate(%s)' % (active, func))
            if active: 
                registry.add(func)
            else:
                registry.discard(func)
            func()
            return None 
        return decorate 
    
    @register(active=False) 
    def f1():
     print('running f1()')
     
    @register() 
    def f2():
     print('running f2()')
     
    def f3():
     print('running f3()')
    
    
    
    print(registry)




if 1==-1:
    
    class Gizmo: # We make this example to proof that a second Gizmo was actually instantiated before the multiplication was attempted and that's why the error occurs
        def __init__(self):
            print("Gizmo's id is %d" % id(self))
            
    Gizmo()
    Gizmo()*10
            


if 1==-1:
    
    Charles = {'name': 'Charles L. Dodgson', 'born': 1832} # We call Charles to an object, in this case a dictionary
    Lewis = Charles # Here is the point we want to look at, we could think that with this move we create a copy of the object and store it on the variable Lewis, but no. We make Charles and Lewis point at the same object, the dictionary.
    print(Charles is Lewis) # True
    Lewis["balance"]=950 # We add the balance feature to the dictionary Lewis is pointing at
    print(Charles) # And because both point at the same object/dictionary, the change made in the line above appears in Charles
    
    Alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
    print(Alex==Charles==Lewis) # It's true because the object Alex points at is similar to the object Charles and Lewis point at, but they are not the same object and we can prove it by the next line
    print(Alex is Charles) # False



if 1==-1:
    t1 = (1, 2, [30, 40])
    t2 = (1, 2, [30, 40])
    print(t1==t2) # True because both objects are similar
    print(t1 is not t2) # True because they are not pointing at the SAME object
    t1[-1].append(99) # t1 is a tuple and inmutable because of that, but t1[-1] is a list, so we can make changes on it
    print(t1==t2) # False because they are not similar anymore


if 1==-1: # And what if we want to create a copy of the object without copying by hand?

    l1 = [3, [55, 44], (7, 8, 9)]
    
    l2 = list.copy(l1) # or  l2 = list(l1)
    print(l2)
    
    print(l1==l2) # Obviously true because they are similar
    print(l1 is l2) # False because they are not pointing at the same object
    


if 1==-1:
    l1 = [3, [66, 55, 44], (7, 8, 9)]
    l2 = list.copy(l1) 
    l1.append(100) # add 100 to the end of l1
    l1[1].remove(55) # remove the 55 of the list inside the position 1 of l1, this also affects to l2, because the inner lists of the list are shared between l1 and l2
    l2[1].append(11) # with this we can prove the afirmation of the upper line
    print('l1:', l1)
    print('l2:', l2)
    l2[1] += [33, 22] # For a mutable object like the list referred by l2[1], the operator += changes the list in place, and l1 and l2 still share the same inner list
    l2[2] += (10, 11) # For unmutable as tuples, the += creates another modified tuple this makes l1 and l2 stop sharing the same inner tuple
    print('l1:', l1)
    print('l2:', l2)




if 1==-1:
    
    from copy import copy, deepcopy
    
    
    class Bus: # Let's create a bus class
    
         def __init__(self, passengers=None): # Add a case for an empty bus (passengers=None)
             if passengers is None:
                 self.passengers = [] # If there's no list with passengers, create one
             else:
                 self.passengers = list(passengers) # If there's one, use it
         
         def pick(self, name):
             self.passengers.append(name) # Pick a passenger by adding to the list
         
         def drop(self, name):
             self.passengers.remove(name) # Drop a passenger by removing from the list
    
    
    
    bus1= Bus(['Alice', 'Bill', 'Claire', 'David'])
    bus1.pick("Alberto")
    bus1.drop("Bill")
    bus1.drop("Claire")
    print(bus1.passengers) # ['Alice', 'David', 'Alberto']
    
    bus2 = copy(bus1) # Bus 2 will be a shallow copy of Bus 1
    bus3 = deepcopy(bus1) # Bus 3 will be a deep one
    
    bus1.drop('David')
    
    print(bus2.passengers) # ['Alice', 'Alberto']
    print(bus3.passengers) # ['Alice', 'David', 'Alberto']
    
    print(id(bus1.passengers)==id(bus2.passengers)) # True because they are the same
    
    print(id(bus1.passengers)==id(bus3.passengers)) # False because they are not the same thanks to the deep copy
    
# Why does this happen? With a shallow copy we copy the structure and share the inner attributes as the passenger list, but with a deep copy we also make a copy of that inner data, making a brand new copy of the same object that shares nothing but qualities




if 1==-1:
    
    a = [10, 20]
    b = [a, 30]
    a.append(b) # We create an infitite cycle of [10, 20, a, 30] where a is [10, 20, a, 30]
    print(a) 
    
    from copy import deepcopy
    
    c = deepcopy(a) # So we can use deepcopy to handle the cyclic references
    print(c)
    
    print(id(a)==id(c)) # False


if 1==-1:
    
    def f (a,b):
        a+=b
        return a
    
    x=1
    y=2
    print(f(x,y))
    print(x) # x is unchanged
    
    a = [1, 2]
    b = [3, 4]
    print(f(a,b))
    print(a) # a list is changed
    
    t = (10, 20)
    u = (30, 40)
    print(f(t,u))
    print(t) # t is unchanged

# What we get out of this is that a function may change a mutable object



if 1==-1:
    
    class HauntedBus: # Similar to the bus class mentioned and explained before
     """A bus model haunted by ghost passengers"""
     
     def __init__(self, passengers=[]): 
         self.passengers = passengers
         
     def pick(self, name):
         self.passengers.append(name)
         
     def drop(self, name):
         self.passengers.remove(name)
    
    
    bus1 = HauntedBus(['Alice', 'Bill']) # We start a bus with 2 passengers
    print(bus1.passengers) # ['Alice', 'Bill']
    
    bus1.pick('Charlie') # We pick Charlie
    bus1.drop('Alice') # Drop Alice
    print(bus1.passengers) # ['Bill', 'Charlie']
    
    bus2 = HauntedBus() # Then start another different bus
    bus2.pick('Carrie') # Pick Carrie
    print(bus2.passengers) # ['Carrie'] all ok yet
    
    bus3 = HauntedBus() # Then start another different bus
    print(bus3.passengers) # It shows us that there's a passenger, this is impossible because we haven't picked anyone up and there werem't people in the bus at the beggining
    bus3.pick('Dave') # Now we pick Dave in bus3
    
    print(bus2.passengers) # ['Carrie', 'Dave'] Dave, picked by bus3, appears in bus2.
    
    print(bus2.passengers is bus3.passengers) # True bus2 and bus3 passengers refer to the same list
    
    print(bus1.passengers) # But bus1 is a completeley different list, what has happened?


# The problem is that Bus instances that don’t get an initial passenger list end up sharing the same passenger list among themselves, this wouldn't have happenned with the anterior model os Bus function, The issue with mutable defaults explains why None is often used as the default value for parameters that may receive mutable values.


if 1==-1:
    
    class TwilightBus:
     """A bus model that makes passengers vanish"""
     
     def __init__(self, passengers=None):
         
         if passengers is None:
             self.passengers = [] 
         else:
             self.passengers = passengers # In the bus class we use list(passengers) and create a copy of the list, in this example, the object will always refer to the external list
             
             
     def pick(self, name):
         self.passengers.append(name)
         
     def drop(self, name):
         self.passengers.remove(name)
    
    
    basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat'] 
    bus = TwilightBus(basketball_team) 
    bus.drop('Tina') 
    bus.drop('Pat')
    print(basketball_team)
    print(bus.passengers)
    print(bus.passengers is basketball_team) # True, the external list becomes the list used by the object, not a copy.



if 1==-1: # We don't want this to happen, we want the object to have it's own internal list and not to refer to a external one, so the model we should follow is this one:

    def __init__(self, passengers=None):
     if passengers is None:
         self.passengers = []
     else:
         self.passengers = list(passengers) # Make a copy of the list




if 1==-1:
    
    import weakref
    s1 = {1, 2, 3} # We start a set
    s2 = s1 # We create another pointer for the set
    
    print(s1 is s2) # True, they point at the same object
    
    def bye():
        print('Gone with the wind...')
    
    ender = weakref.finalize(s1, bye) # Register the bye callback on the object referred by s1
    print(ender.alive) # True, s1 is still alive
    
    del s1 # We delete s1, but just the reference to it, the set hasn't been deleted
    print(ender.alive) # True the object referenced by s1 is still alive
    
    s2 = 'spam' # The "Gone with the wind..." msg appears as the object has been finaly eliminated
    print(ender.alive) # Rebinding the last reference, s2, makes {1, 2, 3} unreachable. It is destroyed, the bye callback is invoked, and ender.alive becomes False.
    


if 1==-1:
    
    import weakref
    
    a_set = {0, 1}
    wref = weakref.ref(a_set) # A weak reference is a callable that returns the referenced object or None if the referent no longer exists
    print(wref) # We print the reference
    print(wref()) # We print the object referred 
    
    a_set = {2, 3, 4} # We change the a_set pointing to another object, causing the original set to be approachless
    print(wref()) # There's no object, it has been deleted by python, if we had a weakref.finalize() the function would have been executed
    print(wref() is None) # True



if 1==-1:
    
    class Cheese:
        
        def __init__(self, kind):
            self.kind = kind
    
        def __repr__(self):
            return 'Cheese(%r)' % self.kind
    
    import weakref
    
    stock = weakref.WeakValueDictionary() # We create a weak value dictionary, so if any of the objects inside it loses every reference, it will be deleted from the list
    catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
    
    for cheese in catalog:
        stock[cheese.kind]=cheese # We add to the weak value dictionary every cheese on the catalog and associate it's own name as the key
    
    print(sorted(stock.keys()))
    
    del catalog # Every cheese on the list loses it's original reference, so they will be aparently eliminated from the weak value dictionary
    
    print(sorted(stock.keys())) # We see that Parmesan is still remaining, but why?
    
    del cheese
    
    print(sorted(stock.keys())) # Finally empty

# What has happenned? the for loop variable cheese is a global variable and will never go away unless explicitly deleted. And that was what provocated that parmesan didn't dissapear from the list.




if 1==-1:
    
    t1 = (1, 2, 3)
    
    t2 = tuple(t1)
    print(t2 is t1) # True. A tuple built from another is actually the same exact tuple
    
    print(t1[1:]) # for a tuple t, t[:] does not make a copy, but returns a reference to the same object
    
    # So, if that's true, the next sequence should be too
    
    t3=t1[:]
    print(t3 is t1) # True
    

    
 if 1==-1:
    
    t1 = (1, 2, 3)
    t3 = (1, 2, 3)

    print(t3 is t1) # This didn't happen like this in the book, but I asume that now if you create two similar tuples in python, the second one becomes the first so there's only one
    # The afirmation above would make sense because tuples are unmutable, so why having two similars if you can't modify them


    s1 = 'ABC'
    s2 = 'ABC'
    print(s2 is s1) # Same happens with str
