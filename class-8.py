        ## ____-----  FUNCTIONS -----____ ##
        
def Greet():  # defining a function
    print("Hello Everyone")
Greet()    # This is calling the function

# return functions - Return is used to tranfer the result at the place from where the function is called
def Greet():  
    return "Hello Everyone"
result = Greet()   
print(result)  # or print(Greet())

# Parameters And Arguments
def addition():
    a = 12
    b = 30
    print(a+b)
addition()  # output- 42


def add(a,b):
    print(a+b)
    
add(10,20)
add(154,86)
add(73,52)

# Check the number is pallindrome number or not 
def pallindrome(x):
    copy = x
    rev = 0
    while x > 0:
        rev = (rev *10) + (x % 10)
        x = x // 10
    if rev == copy:
        return True
    else:
        return False
print(pallindrome(123))
print(pallindrome(121))
        
        
# Keyword argument
def addition(a,b):
    print(a+b)
    
addition(b = 17,a = 18)

# Default paramenter - Default value  of a parameter can be set at last
def add(a,b,c = 12):
    print(a+b+c)

add(23,19)

def add(a, b, c = 22):
    print(a+b+c)

add(23,19,10)

