#Tuples are used to store multiple items in a single variable.
#A tuple is a collection which is ordered and unchangeable.
tuple=("mariyam","ayesha",12,34,56,77,88,9)
print(tuple)


#access tuple items through index
print(tuple[:3])# start 0 index but 3 index not include
print(tuple[-1])#last index


#Change Tuple Values 
#tuple not changable so its convert in list and change value then also convert in tuple

# tuple1 = ("apple", "banana", "cherry")
# y = list(tuple1)
# y.append("orange")
# tuple1= tuple(y)
# print(tuple1)

# #Remove Items
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("orange")
# thistuple = tuple(y)
# print(thistuple)

# Add tuple to a tuple. You are allowed to add tuples to tuples,
thistuple = ("apple", "banana", "cherry")
y = ("orange","mango")
thistuple =thistuple+y

print(thistuple)

#Unpacking a Tuple
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
t=("ayesha","warisha","fizan")#packing tuple
print(t)
#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#Using Asterisk*
# If the number of variables is less than the number of values, you can add an * to the
# variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(*green, tropic, red) = fruits

print(green)
print(tropic)
print(red)

#Loop Tuples
tuple=("mariyam","ayesha",12,34,56,77,88,9)
for i in tuple:
    print(i)
for i in range(len(tuple)):
    print(tuple[i])
#using while loop
i=1
while i < len(tuple):
    
    
    print(tuple[i])
    i=i+1

# join tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
# join multiple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 3

print(mytuple)

# tuple methods 
t = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = t.count(5)

print(x)
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)# return its postion


print(x)