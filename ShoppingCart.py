#Shopping Cart

items = []
price = []
# amount = int(input("How many food you wanna add: "))
while True:
    item = input("Item Name(Enter to quit!): ")
    if item == "q" or item == "Q" or item =="":
        break
    items.append(item)
    try: 
        price2 = float(input(f"Price of {item}: "))
    except :
        price2= float(input("Pls enter an integer: "))

    price.append(price2)
    

print("\n------Your Cart------")   
sum = 0 
for i in range(len(items)):
    print(items[i],": $",price[i])
    sum += price[i] 

print(f"Total Expense: ${sum}")      

    
