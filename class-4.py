        ##  ____----- COMPARISION OPERATORS -----___ ##
        
# It will always print bool (true and false)
# == , != , < , > , <= , >= 

# 1. ==
a  = 10
b = 10
print(a == b) #true
print(10  == 11) #Flase

# 2. !=
print(12 != 12) #false
print(12 != 13) #true

# 3. <
print(12 < 13) #true
print(10 < 2) #false
print(44 <= 44) #true

#4. >
print(12 < 13) #false
print(10 < 2) #true



print((10 == 10) == True) #True
print((10 == 10) != True) #Flase



         ##  ___----- LOGICAL OPERATORS -----____ ##
# operators are 'AND'  and 'OR' and "NOT"

# AND  - one is true and another is false then complete statement is false
print(123 == 123 and 333== 333) # True
print(232 == 232 and 1 == 3 and 23 < 100) # False


# OR - one is true and another is false then complete statement is True
print(10 == 100 or 10 < 100) # True
print( 100 < 99 or 32 == 44) #Flase


# Not - one is true and another is false and print true
print( not 10 == 22 ) #true
print(not 11 == 11 and False) # False
print(not 11 == 11 == False)  #True

print(True and bool(0)) #False
