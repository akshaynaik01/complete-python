       ## Exception Handling ##
# when we run a program in python there are various exceptions that can be raised


a = int(input("Provide your number: "))
b = int(input("Provide your number: "))

try:
    print(a/b)
except Exception as err:
    print(f"Sorry an error occuesd as {err}")
    
else:
    print("There was no errors")
    
finally:
    print("I will execute no matter what !!")

print(a+b)


try:
    age = int(input("Enter age: "))
    if age<18:
        raise Exception("You must be 18+")
    print("Access granted")
except Exception as e:
    print("Error",e)


