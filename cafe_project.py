print("Well_Come To UK-resturant..")

menu = {
    "tea": 20,
    "coffee": 50,
    "cold coffee": 100,
    "vada pav": 30
}

print("\nMENU..!:\nTea :rs20\nCoffee :rs50\nCold coffee :rs100\nVada pav :rs30")

# Default order (CI safe)
order = ["tea", "coffee"]
total_ord = 0

for item in order:
    if item in menu:
        total_ord += menu[item]
        print(f"your item {item} has been added to your order..")

print("\nThe Total amount of items is:", total_ord)
print("THANK_YOU..")
