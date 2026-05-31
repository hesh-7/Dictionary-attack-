#For loops

for x in range(1,11):
    print("HBD",x)

for x in range(1,11,2): #skips 2 steps
    print("HBD",x)

num= "01798793427"
for x in range(0,11):
    print(num[x])


for x in range(1,21):
    if x==15:
        continue #skips 15
    else: 
        print(x)

for x in range(1,21):
    if x==15:
        break #print till 14
    else:
        print(x)        
