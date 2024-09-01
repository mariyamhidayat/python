# task perfrom daily routines 


list=[]

def add():
    num=int(input("please enter how many which you want to perform task"))
    for i in range(0,num):
        a=input("enter  which you want to perform task ")
        list.append(a)
    
    
def update(update_item,item):
    # item:"Where do you want to update? "
    #update_item:what you want to update
    for i in list:
        
        if i ==item:
            x=list.index(item)
            list[x]=update_item
        else:
            "wrong index"
def delete(item):
    for i in list:
        if i==item:
            list.remove(item)
        else:
             "wrong index"
def view():
   
        print(list)
while True:
    print('how many task today perform')

    print("press 1 for add \n press 2 for update , \n,press 3 for delete \n press for 4 view \n  press 5 for exist ")
    i=int(input(" enter a choice which you want to perform operation in list "))
    if i==1:
        add()
        #update
    elif i==2:
            item=input("Where do you want to update? ")
            update_item=input("enter task what you want to update ")
        
            update(update_item,item)
    elif i==3:
        item=(input("enter task which you want to delete "))
        delete(item)

    elif i==4:
        view()
    elif i==5:
        break
print("successfully exist")
