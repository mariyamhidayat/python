#creating functions 
#function to achive re useability modularity and security 
#
def display():#function defination , fun name and body 
    print("this is function")
display()# calling function 
# functions add
def add():#function defination  ,   non -paramertized function 
    print(5+4)
add()# function calling 
def calculation():
    a=int(input("enter the value of a "))
    b=int(input("enter the value of b "))
    sum=a+b
    sub=a-b 
    multipe=a*b
    print(" the sum is ",sum)
    print(" the subtract is ",sub)
  
#number of arguments 
def name(fname,lname):
    print(fname,"",lname)
name("mariyam","hidayat")
#calling functions and display sum
def sum(a,b):
    c=a+b
    return c
sum=sum(a=10,b=20)
print(sum)
#recuerion functions
def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
f=factorial(5)
print("the factorial is ",f)