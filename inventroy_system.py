inventroy={}
def add_inventroy(sr_no,record):
    inventroy[sr_no]=record

def remove_inventroy(sr_no):
    if i in inventroy.keys(): 
        if i==sr_no:
             inventroy.pop(sr_no)
             
             
def update_inventroy(sr_no,update_item):
     for i in inventroy.keys():
        if i==sr_no:
        
          inventroy.update({sr_no: update_item})
def view_inventroy():
    print(inventroy) 
def search_inventroy(sr_no):
    
    for i in inventroy.keys():
        if i==sr_no:
            print(inventroy[sr_no])
        else:
            print("not found")
         
         




while True:
    print("####Inventroy Managment System####")
    print("press 1 add new data in inventroy ")
    print("press 2 remove  data in inventroy ")
    print("press 3 update data in inventroy ")
    print("press 4 search data in inventroy ")
    print("press 5 print inventroy report ")
    print("press 6 exist")
    i=int(input(" enter a choice which you want to perform operation in inventroy"))
    if i==1:
        sr_no=int(input("enter the serial number"))# key
        record=[]
        product_details =input("enter the product details ")
        quantity_purchase=int(input("enter the quantity_purchase  "))
        price=int(input("enter the price of the product"))
        
        record.extend([ product_details,quantity_purchase,price])
        add_inventroy(sr_no,record)

       

    elif i==2:
        sr_no=(input("enter inventroy which you want to delete "))
        remove_inventroy(sr_no)
        

    elif i==3:
         print("if update the product_details press 1 \n update the quantity press 2 \n update price press 3")
         update=int(input("enter choice which you want  update "))
         if update==1:
             product_details=(input("enter product details"))
             sr_no=int(input("enter the sr which  you want update the product_details"))
             update_inventroy(sr_no,product_details)
         elif update==2:
              quantity_purchase=(input("enter quantity"))
              sr_no=int(input("enter the sr which  you want update the product_details"))
              update_inventroy(sr_no,quantity_purchase)
         elif update==3:
              price=(input("enter price"))
              sr_no=int(input("enter the sr which  you want update the product_details"))
              update_inventroy(sr_no,price)
         
     

      
    elif i==4:
        search_item=int(input("enter sr_no which you want to vew"))
        search_inventroy(search_item)
    elif i==5:
        view_inventroy()
    elif i==6:
        break 
print("successfully exist")
   

