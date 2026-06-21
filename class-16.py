   # Deep Attribute and Method

class Animal:
    gender = "Male"
    def __init__(self,name,age):
        self.name = name # instance attribute
        self.age = age  # instance attribute
        
    def info(self):  # instance method
        print("This is a method")
        
    @classmethod
    def clmethod(cls):  #class method
        print(f"{cls.gender} is your gender")
        
    @staticmethod
    def hello():   # static method
        print("Hello I am a static method ")
obj = Animal("Lion",12)

obj.info()

obj.clmethod()

obj.hello()



# Make a student registration system ask for name,age,number,blood grp register 3 student

class Registration():
    def __init__(self,name,age,number,blood):
        self.age = age
        self.name= name
        self.number = number
        self.blood = blood
        
    def info(self):
        print(f"Hello your name is {self.name}\nyout age is {self.age}\nyour number is {self.number}\nyour blood grp is{self.blood}")
        
    
student1 = Registration("Akshay",20,1233217891,"B+")
student2 = Registration("Ankul",25,1233217891,"A+")
student3 = Registration("Akshay",30,1233217891,"O+")

student1.info()
student2.info()
student3.info()
