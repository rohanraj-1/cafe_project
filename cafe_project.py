print(f"Well_Come To UK-resturant..")
menu = {
    "tea" : 20,
    "coffee" : 50,
    "cold coffee" : 100,
    "vada pav" : 30
    }

print("\nMENU..!:\nTea :rs20\nCoffee :rs50\nCold coffee :rs100\nVada pav :rs30")
total_ord = 0

item1 = input("\nplez order a some items :")
if(item1 in menu):
    total_ord += menu[item1]
    print(f"your item {item1} has been added to your order..")
else:
    print(f"Entered itme {item1} is not in menu") 

while True:
    another = input("\nDo you want another items (Yes/No):")
    if another == "no":
        break
    if(another == "yes"):
        item2 = input("Enter the name of another item:")
        if(item2 in menu):
          total_ord += menu[item2]
          print(f"your item {item2} has been added to your order..")
        else:
            print("ordered itme is not in menu")


print("\nThe Total amount of items is:", total_ord)
print("THANK_YOU..")
