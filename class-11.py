# Lambda expression

square = lambda a: a**2
print(square(2))

add = lambda x,y: x+y
print(add(10,20))


# MAP
  # syntax: map(function,iterable)
  
a  = [1,2,3,4]
l = map(lambda x:x**2,a)
print(list(l))

     # using function

def square(x):
    return x**2

a = [1,2,3,4]
l = map(square,a)
print(list(l))


# FIlTER
  # purpose:  Filter items from an iterable based on a condition
  
# syntax - filter(function,iterable)

a = [1,2,3,4,5,6]
l = filter(lambda x : x%2==0,a)
print(list(l))


# ZIP
  # purpose : Combines multiple itreables into pairs of elements.
  
# syntax - zip(iterable1,iterable2,....)

name = ["Akash","John"]
ages = [22,24,23]

comb = zip(name,ages)
print(dict(list(comb)))


# 1.List comprehensions
a = [1,2,3,4,5,6,7,8]
l = [i for i in a if i%2 == 0]
print(l)

# 2. Set comprehensions
a = [1,2,3,4,5,6,7,8]
l = {i for i in a if i%2==0}
print(l)

# 3.Dictionary comprehensions
a = [1,2,3,4,5,6,7,8]
l = {i:i**2 for i in a if i%2==0}
print(l)


#  Genarators : A generator is a function that uses the yield statement to generate values one by one, saving memory and allowing iteration over large sequences efficiently.

def my_generator():
     for i in range(5):
         yield i
gen = my_generator()
print(next(gen))
print(next(gen))
print(list(gen))


# Decorators

def my_decorator(func):
    def wrapper():
        print("hello i will print before")
        func()
        print("hello i will print after")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")
say_hello()


 # example
def decorate(func):
    def wrapper(a,b):
        print("Your 2 number addtion is:")
        func(a,b)
        print("Thank u for using us")
    return wrapper
         
@decorate
def addition(a,b):
    print(a+b)
addition(20,30)
