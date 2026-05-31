#Conditional Expression (ternary operator)

num1 = int(input("Num1: "))
num2 = int(input("Num2: "))

print("Num1 is Positive" if num1>0 else "Num1 is Negative")
print("Num2 is Positive" if num2>0 else "Num2 is Negative")

res1 = f"{num1} is Even" if num1%2==0 else "Num1 is Odd"
res2 = f"{num2} is Even" if num2%2==0 else "Num2 is Odd"
print(f"{num1} is  a {res1} Number")
print(f"{num2} is a {res2} Number")

print(f"{num1} is greater than {num2}" if num1>num2 else f"{num2} is greater than {num1}")
