from random import randint
random_number = randint(1,100)
tries = 0
while True:
    try:
        if tries==0:
            user_guess = int(input("Guess a number between 1 to 100 : "))
        else:

            user_guess = int(input(f"Guess No.{tries+1} : "))
        tries +=1    
            
        
    except:
        print("Invalid Input\nProgramme Exited!")
        quit()
    if user_guess == random_number :
        print("That was a perfect guess!")
        break
    elif user_guess < random_number:
        print("The number is greater than",user_guess)
    elif user_guess > random_number:
        print("The number is less than",user_guess)
print("It took you",tries,"tries to finish!")
