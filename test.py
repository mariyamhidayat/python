#reverse list4
list=[90,89,70,12]

print(list)
#intersection

list1 = ["apple", "banana", "cherry"]
set1=set(list1)

# list2 = ["google", "microsoft", "apple"]
# set2=set(list1)
# set3 = set1.intersection(set2)#Join set1 and set2, but keep only the duplicates:
# list(set3)
# print("unino", list)

#union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)#Join set1 and set2 into a new set
print(set3)
#remove 
tup=(3,4,6,12,55,"maryam","ayesha",4)
# splits 
a1="mariyam hidayat qurat"
print(a1.split())# the separted the string into commas 
# accept list
list=[]
li=int(input("enter the list length"))
for i in range(0,li):
    a=int(input())
    list.append(a)
    
print(list)
list[4]
print(" calculate the fith elements ", list)
if len(list)==8 :
    print("true")
else:
    print("false")
a=list[4]
if list.count(a==3):
    print("true")
tuple=(10,20,30,40,56)
tuple[0:2]
print(tuple)
ep1={1401:23,1402:45,1403:67,1404:78,1405:20}
for i in ep1:
    print(i)

