#Temp conversion
unit = input("Temp unit (C or F):")
unit =  unit.upper()

if unit == "F":
    data = float(input("Enter temp in F: "))
    res = data*5/9-32*5/9
    print(f"{data} in Celcious is {res}")
elif unit == "C":
    data =  float(input("Enter Temp in C: ")) 
    res = data*1.8
    res = res + 32,3   
    print(f"{data} in Fahrenheit is: {res}")
else:
    print("Enter a valid unit.")
