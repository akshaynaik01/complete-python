              ## __--- STRING ---__ ## 

# String indexing

a = "Hello world"
print(a[0]) # H
print(a[-1]) # d

# String slicing
a = "Akshay Naik"

print(a[0:11]) # Akshay Naik
print(a[0:11:1]) #Akshay Naik
print(a[0:11:2]) #Asa ak


# there are default values aswell
print(a[: :]) #Akshay Naik


age = 20
des = "Data Scientist"

print("My name is Akshay Naik, I am ",age,"years of old and I am a ",des)
print(f"My name is Akshay Naik, I am {age} years of old andI am a {des}")

# escape sequence
print("My name is Akshay Naik, I am ",age,"years of old and\n I am a ",des) #\n
print("My name is Akshay Naik, I am ",age,"years of old and\t I am a ",des) #\t
print("My name is Akshay Naik, I am ",age,"years of old and\b I am a ",des) #\b 
print(r"My name is Akshay Naik, I am ",age,r"years of old and\b I am a ",des) 


# type conversion
a = 23
a = str(a)
print(a,type(a)) 

a = float(a)
print(a,type(a))

a = 23.3
a = int(a)
print(a,type(a))

b = "Good morning"
b = bool(b)
print(b,type(b))



# Input Function
name = input("Enter your name: ")
print(f"Hello, my name is {name}")

age = int(input("What is ur age ?"))
print(age,type(a))
