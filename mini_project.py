# student record manage system 
std={}
def std_add(roll_no, record):
    std[roll_no]=record
    return std   
def std_update(roll_no,update):# update marks 
    for i in std.keys():
        if i==roll_no:
          std.update({roll_no: update})
          return std
        else:
            "wrong name"      
def std_delete(roll_no):
     for i in std.keys(): 
        if i==roll_no:
             std.pop(roll_no)
             return std    
        else:
          return "wrong name "     
def std_view_all():
    return std  
def std_view(roll_no):
    for i in std.keys():
        if i==roll_no:
            return std[roll_no]
        else:
            return "wrong roll_no"
while True:
    #menu
    print("press 1 for add \n press 2 for update , \n,press 3 for delete \n press for 4 view \n if view only one tuple press 5 \n press 6 for exist ")
    i=int(input("enter your choice "))
    if i==1:
    #add 
        roll_no=int(input("enter the name (key)"))
        record=[]
        # for i in range(0,4):
        #   r=(input("enter the Name , Address , Age and Marks"))
        #   record.append(r)
        name=input("enter the name ")
        address=input("enter the address ")
        age=int(input("enter the age "))
        marks=int(input("enter the marks "))
        record.extend([name,address,age,marks ])
        std_add(roll_no,record)
    elif i==2:   
         #update 
         print("if update the name press 1 \n update the addree press 2 \n update the age press 3 \n update the marks  press 4 ,")
         update=int(input("enter choice which update "))
         if update==1:
             name=(input("enter update name"))
             roll_no=int(input("enter the roll_no which  you want update the name"))
             std_update(roll_no,name)
         elif update==2:
             address=(input("enter update address"))
             roll_no=int(input("enter the roll_no which  you want update the address"))
             std_update(roll_no,address)
         elif update==3:
             age=(input("enter update age"))
             roll_no=int(input("enter the roll_no which you want update the age"))
             std_update(roll_no,age)
         elif update==4:
             marks=(input("enter update marks"))
             roll_no=int(input("enter the roll_no which  you want update the marks"))
             std_update(roll_no,marks)
    elif i==3: 
        # delete 
         print("if delete the name press 1 \n delete the address press 2 \n delete the age press 3 \n delete the marks  press 4 ")
         roll_no=int(input("enter delete the roll number"))
         std_delete(roll_no)

        #  if delete==1:
        #      name=(input("enter delete name"))
        #      roll_no=int(input("enter the roll_no which you want delete the name"))
        #      std_delete(roll_no)
        #  elif delete==2:
        #      address=(input("enter delete address"))
        #      roll_no=int(input("enter the roll_no which you want  delete the address"))
        #      std_delete(roll_no,address)
        #  elif delete==3:
        #      age=(input("enter delete age"))
        #      roll_no=int(input("enter the roll_no which delete the age"))
        #      std_delete(roll_no,age)
        #  elif delete==4:
        #      marks=(input("enter delete marks"))
        #      roll_no=int(input("enter the roll_no which you want  delete the marks"))
        #      std_delete(roll_no,marks)
    elif i==4:
        # view  all 
       print( std_view_all())    
    elif i==5:
        # if view only one tuple
        roll_no=int(input("enter the roll_no which you want views the data "))
        print(std_view(roll_no))
    elif i==6:
        break
print("exist it successfully")


