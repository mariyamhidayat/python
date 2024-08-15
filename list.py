#create list
list=[10,20,"mariyam",40,"sumeria",90,89]
print(list) 
# find length
print("display the length",len(list))
# according to index access list item
print("according to index",list[1:5])#1 add but 5 not add
print(list[6:])#only print 6 index value
print(list[:5])# first 4 value print
print(list[-1])# -1 show last item in list
print(list[-4:-1])
#Check if Item Exists
if "mariyam" in list:
    print("yes")
else:
    print("no")
#Change Item Value
list[3]="hidayat"
print(list)
list[0:3]="aiza","sameen","mariya"
print(list)

# add item in list
list.append("uzma")# add end of the list
list.extend(["hammad","rehman","ayesaha"]) # add values end of list
print(list)
list.insert(1,"aaa")# add value according to index which means 1 is index
print(list)

# remove items in list
list.remove("hammad")
list.pop(0)#Remove Specified Index
list.pop()#remove last index
print(list)
delete=[10,20,30,50]
del delete # delete the list


# use loops in list
for i in list:
    print(i)
# function
list1=[90.80,70,45,24,1,78]
list1.sort()#sort function
print(list1)
list1.sort(reverse=True)# reverse function
print(list1)
list2=list1.copy()
print(list2)

# joins two list
num=[100,200,300,400,500]
num2=[40,60,80]
num3=num+num2
print(num3)

# creat the list form the user
list=[]
ra=int(input("enter the range of the list"))
for i in range(0,ra):
    li=int(input())
    list.append(li)
print(list)