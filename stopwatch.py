import time
import os


tim = int(input("Enter stopwatch time: "))

for x in range(tim,0,-1):
    sec = x%60
    min = int(x/60)%60
    hr = int(x/3600)
    days = int(x/(3600*24))
    print(f"{days:02}:{hr:02}:{min:02}:{sec:02}")# :02 will show 0 if nothing is there.
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear') #to clear the terminal
print("Time is up!")    
