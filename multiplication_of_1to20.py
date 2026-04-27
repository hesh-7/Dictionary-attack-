#This programme will generate 20 file
# containing multiplication table of 
# numbers beginning from 1 to 20
for i in range(21):
    for j in range(11):
        a=open(f"mulof{i}","a")
        a.write(f"{i} x {j} = {i*j}\n")
