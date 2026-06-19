   ## OOPS in Python ##
   
# Imperative Programming
a = 10
b = 5
print(a+b)

# Functional Programing
def addition(a,b):
    print(a+b)
addition(12,14)

# OOPs
class addition:
    def __init__(a,b):
        print(a + b)
obj = addition(10, 10)


# Class
 # class is the blue-print of the object
 
class Factory:
    a = 12  # attribute
    def hello():# method
        print("How are you")
    
    print("I am get initialized")
    
print(Factory.a)
Factory.hello()
 
# Object
 # We use class blueprint to make an object
 
class Factory:
    a = "Hello I am a attribute"
    def hello(s):
        print("Hello I am a method")
        
obj = Factory()  # obj becomes an object who can access anything inside the class till now 
obj2 = Factory()

print(obj.a)
obj2.hello()
    
    

# Constractor
 # A construtor is a method that run automatically whenever we call the class.
 
class Factory:
    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets
        
    def showdetails(self):
        print(self.material,self.zips,self.pockets)
        
reebok = Factory("Leather", 3, 3)
campus = Factory("Nylon",2,2)  
   
print(reebok.material)   
print(campus.material)

reebok.showdetails()
campus.showdetails()


