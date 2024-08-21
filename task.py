#ind factorial using recusive function
def isfactorial(a):
    if a==0 or a==1:
        return 1
    else:
        fa=a*isfactorial(a-1)
        return fa
a=int(input("enter the number to find factorial "))
fact=isfactorial(a)
print("the factorial is ",fact)
# find factorial without function
# a=int(input("enter the number to find factorial ")) 
# fact=1
# if a==0 or a==1:
#       print(1)
# else:
#      for i in range(2,a+1):
#         fact=fact*i
# print(fact)

# # create a function that accept any argument and then print
# def add(*num3):
#      sum=0
#      for i in num3:
#           sum=sum+i
#      return sum    
# res=add(5,5,6)
# print(res)
# # 2nd create a function calculation and perform add and subtract and retun single 
# def calculation(a,b):
#      return a+b,a-b
# res=calculation(10,20)
# print(res)
# # 3rd  create a function of empolyee print the salary and name
# def employee(name=0,salary=0):
#      print("the name of employee ",name,"the salary of employee",salary)
# employee("hammad",60000)

# # create the outer and function having 2 paramter  and add and inside inner function add +5 and return
# def outerfun(a,b):
#      add=a+b
#      r=innerfun(add)
#      print("the outer function ",r)
    
#      def innerfun(add):#  calculate addition 
#           sum=add+5
#           return sum
# outerfun(10,15)
#6 
def calculation(std_name,std_age):
    print("stduent name",std_name,"student age",std_age)

calculation("mariyam",45)

#7 print list of the even number range 10 51
list=[]
for i in range(10,51):
    if i%2==0:
     list.append(i)
print(list)
#8 find max number 
x=[4,6,8,24,12,2]
print(max(x))          