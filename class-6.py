           ## ___----- Loops -----___ ##
# when we want top perform repetitive tasks we use loops
'''
types of loops :- for loop , while loop
for loops :- I is used when you know till where u wanna go
while loops :- It is used with conditions
 
'''

#  For loop - range(start,stop,step)
for i in range(1,11,1):
    print(i) 

ran = range(1,10,1)
for i in ran:
    print("Hello! How are u all")
    

# Print number from 10 to 40
for i in range(10,41,1):
    print(i)
    
# Print number from -10 to 20
for i in range(-10,21,1):
    print(i)
    
#Print number from 34 to 5
for i in range(34,4,-1):
    print(i)
    
# Print the given table
n = int(input("Tell the number u want table of:-  "))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")
    
    # OR
    
n = int(input("Tell the number u want table of:-  "))
for i in range(n,(n*10)+1,n):
    print(f"{n} * {i//n} = {i}")


# For strings
s = "How are u all" # first way
for i in s:
    print(i)

for i in range(0,len(s),1):
    print(s[i])
    

# Default Values
for i in range(11):
    print(i)  # it will print 1 to 10 number
    
a = "Nature"
for i in range(len(a)):
    print(a[i])
    
    
               ## PROBLEMS ##

# 1. Print "Hello World" n time
# Use a loop to repeat a print statement ("Hello World") based on user input count n.
n = int(input("Tell me how many time u want to print:- "))
for i in range(n):
    print(f"{i+1} : Hello wolrd")
    
# 2. Print Number 1 to n. 
# dispaly number in increasing order from 1 up to give number n.
n = int(input("Tell where u want your number:- "))
for i in range(1,n+1):
    print(i)

# 3. Print  Number n to 1. 
# dispaly number in decreasing order from n down to 1.
n = int(input("Tell where u want your number:- "))
for i in range(n,0,-1):
    print(i)
    
# 4. Sum of natural numbers(1 to n)
# Take input n and calculate the total sum from 1 to n
n = int(input("Till where u want sum:- "))
s = 0
for i in range(1,n+1):
    s = s + i
print(f"Your sum is {s}")

# 5. Factorial of a Number
# calculate the factotial (n!) using a loop - multiplying number from 1 to n.
n = int(input("Which  number factorial you want:- "))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(f"Factorial of {n} is {fact}")

# 6. Sum of Even & Odd Number in range
# From 1 to n, find and print the sum of all even and all odd number separately.
n = int(input("Enter a range:- "))
even_sum = 0
odd_sum = 0

for i in range(1,n+1):
    if i % 2 == 0:
     even_sum = even_sum + i
    else:
        odd_sum +=  i
    
print(f"Hello your even sum is {even_sum} and your odd sum is{odd_sum}")
     
# 7. Print all factors of a number
# Display all number that divide the input number exactly (no remainder).
n = int(input("What number factors I want to find:- "))

for i in range(1,n+1):
    if n % i == 0:
        print(i)
        
# 8. Sum of all factors
# Add up all the factors found in the previous question(excluding or including the number itself - your choice).
n = int(input("What number factors sum u want:- "))
sum = 0
for i in range(1,n+1):
    if n % i == 0:
        print(i)
        sum +=  i
print(f"Your factors sum is {sum}" )

#9. Power calculation(a^b)
# Input base a and exponent b,calculate the result using a loop (without using **)
a = int(input("Enetr a value:- "))
b = int(input("Enter a exponent:- "))
power = a
for i in range(b-1):
    power = power * a
print(power)

# 10.Prime number check
# Accept a number check if it is divisible only by 1 and ifself (i.e,prime or not)
n = int(input("Give your number (prime check):- "))
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count += 1
if count == 1:
    print("Your number is a unity number")
elif count == 2:
    print("Your number is prime number")
else:
    print("Your number is composite")
    
       #or#
n = int(input("Give your number (prime check):- "))
for i in range(2,n):
    if n % i == 0:
        print("Sorry your number is composite")
        break
    else:
        print("Your number is prime")
