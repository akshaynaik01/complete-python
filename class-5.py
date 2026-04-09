          ## ___----- CONDITIONAL STATEMENT -----___ ##
          
# if else statement
age = int(input("Enter ur age :- " ))
if age>=18:
    print("U are eligible to Vote")
else:
    print("U are not eligible vote")
    
#  pass
age = int(input("Enter ur age :- " ))
if age>=18:
    pass
else:
    print("U are not eligible vote")


# ternary operation
age = int(input("Enter ur age :- " ))
print("vote") if age >=18 else print("Not vote")


# Elif statement
money = int(input("Please give me 10,20 or 30 rs above: "))
if money == 10:
    print("I will have a choco bar")
elif money == 20:
    print("I will have a mango dolly")
elif money == 30:
    print("I will have a cone")
else:
    print("I will have full course meal")
    
 
# Logical operator
a = 10
b = 40
c = 30

if a > b and a > c:
    print("A is the largest number ")
elif b > a and b > c:
    print("B is a largest number")
else:
    print("C is a largest number")
    
    
#1.Take 2 input and which is greater than or equal
a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))

if a == b:
    print("A and B both are equal")
elif a > b:
    print("A is greater then B")
else:
    print("B is greater then A")
    
#2.Greet by Gender
#Accept a gender input (m or f) and print a greeting like "Hello Sir" and "Hello Mam"
gen = input("Enter your gender(m/f):- ")
if gen ==  "m":
    print("Hello Sir")
else:
    print("Hello Mam")
    
#3. Gender with case handling
# make the gender check case- insensitive('m','f','M','F' all valid).if input is invalid, print "Wrong input"
gen = input("Enter your gender:- ")
if gen == 'm' or gen == 'M':
    print("hello sir")
elif gen == 'f' or gen == 'F':
    print("Hello mam")
else:
    print("Wrong Input") 


#4. Even or odd
num = int(input("Enter a number:- "))
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is odd ")
    
#5. Voting Eligible
name = input("Enter Your Name:- ")
age = int(input("Enet your age:- "))
if age >=18:
    print(f"Hello {name} u can Eligible to vote")
else:
    print(f"Sorry {name} u are not eligible to vote. Wait for {18 - age} yr ")


#6. Day number to day name
Day = int(input("Enter day number(1-7):- "))

if Day == 1:
    print("Moday")
elif Day == 2:
    print("Tuesday")
elif Day == 3:
    print("Wednesday")
elif Day == 4:
    print("Thusday")
elif Day == 5:
    print("Friday")
elif Day == 6:
    print("Saturday")
elif Day == 7:
    print("Sunday")
else:
    print("Wrong input")
    
#7. Greatest of three numbers
# accept three number and find the greatest one among them using nested if-else
a = int(input("enter 1st number:- "))
b = int(input("enter 2nd number:- "))
c = int(input("enter 3rd number:- "))

if a == b  and b == c:
    print("All are equal")
elif a > b and a > c:
    print("A is greater")
elif b > a and b > c:
    print("B is greater")
else:
    print("C is greater")
    
#8. Leap year checker
# input a year and check if its a leap year using proper rules: divisible by 4, not by 100 unless divisible by 400
year = int(input("Enter year :- "))

if year % 100 == 0 and year % 400 ==0:
    print(" leap year")
elif year % 100 != 0 and year % 4 ==0:
    print(" leap year")
else:
    print("Not a Leap yr")
    
#9. Shop discount calculator
bill = int(input("enter a total amount:- "))
if bill >= 1000 and bill <= 4999:
    print(f"u got a discount of 10% ur final amount is {(bill*90)/100} ")
elif bill >= 5000:
      print(f"u got a discount of 20% ur final amount is {(bill*80)/100} ")
else:
    print("Sorry no discount for u")
    

#10. vowel and consonant
char = input("Tell ur alphabet:- ")
#if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U' 
if char in "aeiouAEIOU":
    print("its a vowel")
else:
    print("its a consonant")
