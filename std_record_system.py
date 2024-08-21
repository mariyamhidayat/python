# student record manage system 
std={}
def std_add(name, marks):
    std[name]=marks
    return std
    
def std_update(name,marks):# update marks 
    for i in std.keys():
        if i==name:
          std.update({name: marks})
          return std
        else:
            "wrong name"
       
def std_delete(name):
     for i in std.keys(): 
        if i==name:
             std.pop(name)
             return std    
        else:
          return "wrong name "
     
      
def std_view():
    for x,y in std.items():
        return x,y
    


while True:
    #menu
    print("enter 1 for add , enter 2 for update , enter 3 for delete , enter for 4 view , enter 5 for exist ")
    i=int(input("enter your choice "))
    if i==1:
        name=(input("enter the name (key)"))
        marks=int(input("enter the value"))
        std_add(name,marks)

    elif i==2:
         n=(input("enter update name"))
         m=(input("enter update marks"))

         
         std_update(n,m)
         print(std)
    elif i==3:
        n1=(input("enter delete  name"))
        std_delete(n1)
        print(std)
    elif i==4:
        std_view()
        print(std)
    elif i==5:
        break
print("exist it successfully")
    



    
        
        
#   s=int(input("enter the students range "))
#     for i in range(s):
#       name=(input("enter the name of student"))
#       marks=int(input("enter the marks "))
#       std[name]=marks
#     return std
# def std_update():







  