#Apartment calculator
def appartment_calculator():
  rent=int(input("enter the rent of the apartment"))
  utlity_bill=int(input("enter the utlity bill of the apartment "))
  fast_food=int(input("enter the total fast food expenses "))
  person=int(input("enter the number of persons in apartment"))
  total_cost=(rent+utlity_bill+fast_food)/person
  print("total cost per person", total_cost)

appartment_calculator()

