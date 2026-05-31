#Compound interest generator

principal = float(input("Enter Principal: "))
while principal <=0:
    principal = float(input("Principal cant be 0 or less\nEnter again:"))

rate = float(input("Enter Rate(%): "))
while rate<=0:
    rate = float(input("Rate cant be 0 or less\nEnter again(%): "))

time =  float(input("Enter time: "))
while time<=0:
    time = float(input("Time cant be 0 or less\nEnter again: "))

total = principal * pow(1+rate/100, time)

print(f"Total value after {time} year(s) at {rate}% interest rate is ${round(total,2)}")
