 ## WHILE LOOP ##

a = 0
while a <= 10:
    print(a)
    a = a + 1  # it will print 0 - 10
    

a = 10
while a >= 0:
    print(a)
    a = a - 1   # it will print 10 - 0
    
# Break
for i in range(1,11):
    print(i)
    if i == 6:
        break   # it will print 1 - 6
 
a = 1
while a<=10:
    print(a)
    a += 1
    

# Continue

for i in range(1,11):
    if i == 6:
        continue
    print(i) 
    
    
# else

for i in range(1,5):
    if i == 8:
        break
    print(i)
else:
    print("No break executed")
    
    
    ## PROBLEMS ##
    
# 1. Print each digit(reverse order)
#Break a number into individual digit and print them starting from the last digit
a = int(input("Enter the number:- "))

while a > 0:
    print(a % 10)
    a = a // 10
    
# 2. Sum of digits
# Add all the digits of a number
a = int(input("Enter the number:- "))
s = 0
while a > 0:
    s = s+ a % 10
    a = a // 10
print("Your digit sum is ",s)

# 3. Reverse a number
# Input a number abd reverse its digits
a = int(input("Enter the number:- "))
rev = 0
while a > 0:
    rev = rev * 10 + a%10
    a = a // 10
print("Your number reverse is ",rev)

# 4. Palindrome number check
# check if a number reads the same forward and backward
a = int(input("Enter the number:- "))
copy = a
rev = 0
while a > 0:
    rev = rev * 10 + a%10
    a = a // 10
if rev == copy:
    print("Yes your number is Palindrome")
else:
    print("Sorry your number is not a palindrome")
    
# 5. Automorphic number 
# A number is automorphic if its square ends with the number itself
a = int(input("Enter the number:- "))
copy = a
square = a ** 2
count = 0

while a > 0:
    count += 1
    a = a // 10
extract = square % (10**count)  
if extract == copy:
    print("Your number is automorphic ")
else:
    print("Your number is not a automorphic ")
