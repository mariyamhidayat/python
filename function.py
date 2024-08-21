def add():#function defination 
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
    print(" the multiple is ",multipe)
calculation()
# calling function which take is called arguments 

# find prime number 
def isprime(a):
    for i in range(2,a):
        if(a%i==0):
            print(" not prime")
            break
    else:
        print("prime")
a=int(input("enter the input and find number is prime or not"))
isprime(a)


# find factorial 
def isfactorial(a1):
    if a1==0 or a1==1:
        return 1
     
    else:
        return a1*isfactorial(a1-1)
       
a1=int(input("enter the input find the factorial"))
fact=isfactorial(a1)
print(fact)

# another way find factorial
a2=int(input("enter the input find the factorial"))

fac=1
if a1==0 or a1==1:
        print(1)
else:
     for i in range(1,a2+1):
        fac=fac*i
     print(fac)




#find perfect number

def isperfect(a2):
    sum=0
    for i in range(1,a2):
      rem=a2%i
      if rem==0:
        sum=sum+i
    if sum==a2:
       print("perfact number")
    else:
       print("not perfect")  
 

a2=int(input("enter the input find perfect number"))
isperfect(a2)

# find fab
def Fibonacci(n):

	# Check if input is 0 then it will
	# print incorrect input
	if n < 0:
		print("Incorrect input")

	# Check if n is 0
	# then it will return 0
	elif n == 0:
		return 0

	# Check if n is 1,2
	# it will return 1
	elif n == 1 or n == 2:
		return 1

	else:
		return Fibonacci(n-1) + Fibonacci(n-2)


# Driver Program
print(Fibonacci(6))

  # another way find febonacci number
n1=0
n2=1
n4=0
a2=int(input("enter the input find febonacci number"))
for i in range(2,a2):
    n3=n1+n2
    print(n3)
    n1=n2;    
    n2=n3
    n4=n4+n3 
print(n4) 






# postional arguments sequence matter in postional agrument
def fullname(fname,mname,lname):
     print(fname,mname, lname)
fullname("ayesha","khan","sarfraz")

#keyword arguments arguments sequence doesnot  matter in postional agrument
def keyword_agr(name,age, *phone_no):# * use as a tuple
     print(name,age,phone_no)
keyword_agr("mariyam",34,"023998","023456")

#default arguments 
def add(n=0,n1=0):
     print(n+n1)
add(5,9)

def fullname(fname="mariyam",mname="hidayat",lname="ullah"):
     print(fname,mname, lname)
fullname("ayesha","sarfraz")

# return function
def add(a,b):
     return a+b
res=add(3,4)
print(res)
#Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)
    #print(food)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)


# function used as a variable 
def increment(x):
    x=x+1
    return x
def decrement(x):
    x=x-1
    return x
res=increment(12)+decrement(10)
print(res)


#local varible and global variable are used inside and outdide 
# 4 types of user define function
# Function with no arguments and no return value
def name():
    print("abc")
name()# no argument , no return vale 
# Function with no arguments and a return value

def name():
    return "xyz"
r=name()# no argument , return vale 
print(r)
# Function with arguments and no return value
def name(name):
    print(name)
name("mariyam")# with argument , no return vale 
# Function with arguments and with return value

#lambda function 
# a is agrument and a+10 is expression
lam=lambda a :a+10
print(lam(5))
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))








#software a collection of program is called software 
# 