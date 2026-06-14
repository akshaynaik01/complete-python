            ## Dictionary ##
# Defination : It is also used ti store multiple values but unlike sets, it stores data in key-value pairs
# It is mutable
# we don't add duplicate key ,add duplicate values
d = {"key":"Value"}
print(type(d))

d = {10:100,20:200,30:300,40:400}
print(d[10])

d[10] = 100.00    #update value
print(d)


#constract dictionary
#Type 1.
d = dict(name = "Sam",age = 20,gender = "Male")
print(d)

#Type 2.
d = dict([("name","Sam"),("age",24)])
print(d)


# Trasversing
a = {10:100,20:200,30:300,40:400}
for i in a:
    print(i) #only keys
for i in a:  # or  for i in a.values():
    print(a[i]) # only values
    
    # methods
help(dict)
print(a.get(10))
print(a.items())
print(a.keys())

a.pop(10)
print(a)
popped = a.popitem()
print(popped)

a.setdefault(12)
print(a)

a = {10:100,20:200,30:300,40:400}
b = {40:400,50:500,60:600,70:700}
a.update(b)
print(a)



   ### Problems ###

#1. Print unique elements in array
a = [1,1,1,2,2,2,3,3,3,3,4,4,4,5,5,5,6,6,6,7,7]
d = {}
for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

print(d.keys())

#2. Count frequency of array elements
a = [1,1,1,2,2,2,3,3,3,3,4,4,4,5,5,5,6,6,6,7,7]
d = {}
for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
print(d)


#3. Check if 2 strings have same frequency map
s1 = "aabbcc"
s2 = "kbaccab"

if len(s1) == len(s2):
    d = {}
    for i in s1:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    for i in s2:
        if i in d.keys():
            d[i] -= 1
        else:
            print("An extra element found")
    for i in d:
        if d[i] != 0:
            print("Sorry ur  elements are not same")
            break
    else:
        print("Your strings are same ")
else:
    print("Not same")
 
#4. Find duplicated in array using hash function
a = [1,2,1,2,4,3,3,7,5,0,6,3,1,2,4,2,7,2,]
d = {}
for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

for i in d:
    if d[i] > 1:
        print(i)
