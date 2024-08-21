dic={
    1401:"mariyam", 1402:"meerab",1403:"ayesha",1404:"sumeria",1404:"hamna"
}
print(dic)
# acess according to key
print(dic[1401])
print(dic.keys())
print(dic.values())
print(dic.items())
# find length
print(len(dic))
#The dict() Constructor
dic1=dict(name = "John", age = 36, country = "Norway")
print(dic1)
#update dictionary 
ep1={1401:23,1402:45,1403:67,1404:78,1405:20}
ep2={1501:93,1502:48,1503:97}
ep1.update(ep2)
print(ep1)
#change items 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)
#add items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
# remove items 
ep1={1401:23,1402:45,1403:67,1404:78,1405:20}
ep2={1501:93,1502:48,1503:97}
ep1.pop(1401)
ep1.popitem()# remove last items in dic
print(ep1)
ep3={}# create the empty dictinary 
print(ep3)
# add data in empty dictionary 
ep3.update({1501:93,1502:48,1503:97})
print(ep3)

#loops
dic={
    1401:"mariyam", 1402:"meerab",1403:"ayesha",1404:"sumeria",1404:"hamna"
}
for i in dic:
    print(i)#print keys 
    print(dic[i])# print values
# print values 
print("values")
for i in dic.values():
    print(i)
print("keys")
for i in dic.keys():
    print(i)
#both keys and values
print("both keys and values")
for x,y in dic.items():
    print(x,y)
    
#nested dictionary
# creat three dictionaries
std1={"rol_name":1201,"name":"mariyam","email":"abc","address":"ttts"}
std2={"rol_name":1202,"name":"ayesha","email":"ach","address":"tsfs"}
std3={"rol_name":1203,"name":"zainab","email":"asj","address":"jgs"}
cls={"std1":std1,"std2":std2,"std2":std2}
print(cls)

# methods

#copy
std1={"rol_name":1201,"name":"mariyam","email":"abc","address":"ttts"}
std2=std1.copy()
print(std2)
#get
print(std1.get("name"))# use the key and acess value 
#items
print(std1.items())
#fromkeys
#Create a dictionary with 3 keys,
key=(1,2,3)
value=("a","b","c","d")
print(dict.fromkeys(key,value))

#How To Add User Input To A Dictionary
dic={}
a=int(input("enter the range of dictionary"))
for i in range(a):
    key=int(input("keys"))
    values=(input("values"))
    dic[key]=values
print(dic)



