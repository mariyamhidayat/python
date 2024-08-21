# modules 
# 1factorial 
def isfactorial(a1):
    if a1==0 or a1==1:
        return 1
     
    else:
        return a1*isfactorial(a1-1)

# 2find sum subtract and multiplication 
def calculation():
    a=int(input("enter the value of a "))
    b=int(input("enter the value of b "))
    sum=a+b
    sub=a-b 
    multipe=a*b
    return sum , multipe, sub 
    
#3 find even number 
def even():
    list=[]
    for i in range(0,100):
        if i%2==0:
            list.append(i)

    return list


# 4find odd number 
def odd():
    list=[]
    for i in range(0,100):
        if i%2==1:
            list.append(i)

    return list

# 5find perfect number 
def isperfect(a2):
    sum=0
    for i in range(1,a2):
      rem=a2%i
      if rem==0:
        sum=sum+i
    if sum==a2:
       return "perfect"
    else:
       return "not perfect "

#6 find prime number 
def isprime(a):
    for i in range(2,a):
        if(a%i==0):
            return "not prime"
            break
    else:
        return "prime"

#7 fabonacci number  # series 0,1,1,2,3,5,8,11.....
def fabancci(x):
    list=[]
    n1=0
    n2=1
   
    for i in range(0,x):
       
        n3=n1+n2  # 0+1
        list.append(n3)#1
        n1=n2
        n2=n3
        
    return list

#
def gct():
    a=30
    b=21
    while a!=b:
        if a>b:
            a=a-b

        elif b>a:
            b=b-a
    return a

        




  

  


