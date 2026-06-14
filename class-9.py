 ## _____----- Data Structure -----______ ##

# List
a = []
print(type(a))

a = [1,1.1,12j, 'hello',True,print(),str()]
# U can store anything inside a list
#Hetrogenous Nature
# List is mutable that means you can change anything
# list Can also store duplicates

print(a)


l = [10,20,30,40,50]
print(l[0]) # indexing

print(l[0:2]) # slicing

a = [10,20,30,40]
a[0] = 15
print(a)   # mutable

#reference copy
a = [10,20,30,40]
b = a
b[0] = 100
print(a)
print(b)

#shallow copy
a = [10,20,30,40]
b =a.copy()
b[0] = 100
print(a)
print(b)

#deep copy
import copy

a = [10,20,30,40]
b = copy.deepcopy(a)
b[0] = 100
print(a)
print(b)

#Traversing method 1
a = [10,20,30,40]

for i in range(len(a)):
   print(i) 

#Traversing method 2
a = [10,20,30,40]

for i in range(len(a)):
   print(a[i] ) 
   
# Methods
#  help(list)
#append
a =[10,20,30,40]
a.append(50)
print(a)

#clear
a.clear()
print(a)

#count
a = [10,20,10,20,30,40,10]
print(a.count(10))

#index
print(a.index(30))

#POP
a = [10,20,30,40]

popped = a.pop(0)
print(a)
print(popped)


# PROBLEMS
# 1. sum and average of list
a = [10,20,30,40]
sum = 0
for i in a:
   sum = sum + i
print(f"Sum of your list number is {sum}")
print(f"Average of your list number are{sum/len(a)}")

# 2.Maximum element with index
a = [10,30,2,50,65,20,44,12]
max = a[0]
index = 0
for i in range(len(a)):
   if a[i] > max:
       max = a[i]
       index = i
print(f"Maximum elemnt is {max} at index {index} ")

# 3.Find Second greatest element 
a = [10,30,2,50,65,20,44,12]
max = a[0]
max2 = a[0]
index = 0
index2 = 0
for i in range(len(a)):
   if a[i] > max:
       max2 = max
       max = a[i]
       index2 = index
       index = i
   elif a[i] > max2:
       max2 = a[i]
       index2 = i
       
print(f"max {max} at {index} and max2 is {max2} at {index2}")

#4. Check if list is sorted(Increasing)
a = [26,32,42,49,59,60,66]
for i in range(len(a)-1):
    if a[i] < a[i+1]:
        continue
    else:
        break
else:
    print("Your list sorted")
         
#5. Left rotation by 1
a = [10,20,30,40,50]
for i in range(len(a)-1):
    a[i],a[i+1] = a[i+1],a[i]
    
print(a)

#6. Right Rotation by 1
a = [10,20,30,40,50]
for i in range(len(a)-1,0,-1):
    a[i],a[i-1] = a[i-1],a[i]
    
print(a)

#7.Left rotation by k
k = int(input("How many Times u  want to rotate: "))
a = [10,20,30,40,50]
for i in range(k):
    for i in range(len(a)-1):
        a[i],a[i+1] = a[i+1],a[i]
        
#8. Linear Search
a = [2,36,74,53,21,48,77,36,54]
search = 48
for  i in range(len(a)):
    if a[i] == search:
        print(f"Element found at index {i}")
        break
else:
    print("Sorry no such element exits")
        

#9. Binary Search
a = [12,13,14,16,19,25,28,30,34,39,45,47,49,50,51,57,66,73,79,80]
search = 100

start = 0
last = len(a)-1


while start<=last:
    mid = (start+last)//2
    if a[mid] == search:
        print(f"Element found at index {mid}")
        break
    elif a[mid] < start:
        start = mid + 1
    elif a[mid] > search:
        last = mid-1
        
else: 
    print("No such element exist ")
    

#10. Bubble Sort
a = [34,26,89,12,16,33,11]
for j in range(len(a)-1):
    for i in range(len(a)-1-j):
        if a[i] > a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
print(a)

#11.Selection Sort
a = [34,26,89,12,16,33,11]

for i in range(len(a)-1):
    j = i+1
    min = i
    for k in range(j,len(a)):
        if a[k] < a[min]:
            min = k
    a[i],a[min] = a[min],a[i]
    
print(a)
