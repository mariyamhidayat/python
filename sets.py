set={10,20,30,40,50,60}
print(10 in set)# check exist or not
# add data items in set
set.add(900)
print(set)
#Add Sets
a={'a','b','c','d'}
b={'x','y','z'}
a.update(b)# set b add in set a
print(a)
#Add elements of a list to at set:
list=[1,2,3,4,5]
a.update(list)
print(a)
#using loop
for i in list:
    print(i)

# remove 
re={10,"mariyam","ayesha",20,30}
re.remove("mariyam")
re.discard(10)#remove
print(re)
del re# del keyword will delete the set completely

#method


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)#Join set1 and set2 into a new set
print(set3)#use the | operator instead of the union() method

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)#Join set1 and set2, but keep only the duplicates:
print(set3)#use the & operator instead of the intersection() 

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)#set1 k whose elements which are not set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)# method will keep only the elements 
#that are NOT present in both sets. use operator ^
print(set3)
# isdisjoint    Return True if no items in set x is present in set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)
#intersection_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y) # x update ho giya ha 

print(x)
# 

