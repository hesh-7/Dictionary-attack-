from time import time,sleep
from os import system,name
# import matplotlib as mlt
from random import randint,choice
def ran_words(h_m_w_u_w_t_t):   #h_m_w_u_w_t_t = How many words the user wants to type.
    with open("random_words.txt","r") as f:
        f=f.read()
        list=f.split()
        len_list=len(list)

    l=""
    for i in range(0,h_m_w_u_w_t_t):
        random_word=choice(list)
        l+=" "+random_word
        l=l.strip()
    return l


def clear():
    if name=="nt":
        _=system("cls")
    else:
        _=system("clear")
        
what_user_wants_to_type=input("A : Random words ?\nB : A Paragraph/Story?\n").lower()

if what_user_wants_to_type=='a':
    try:
        how_many_words_user_wants_to_type=int(input("How many words you wanna type : "))
    except Exception as E:
        print("Invalid Input :",E)
    str=ran_words(how_many_words_user_wants_to_type)
elif what_user_wants_to_type=='b':
    pass

str_list=str.split()
lenOf_words_str=len(str_list)
enter=input("Hit enter to begin!")
if enter =="":
    print("One/")
    sleep(1)
    print("Two//")
    sleep(1)
    print("Three///")
    sleep(1)
    print("Go!")
    clear()
else:
    print("Are you an idiot?")
    exit()

while True:
    print("Type the following sentence : ")
    print(str)
    start_time=time()   
    user_input=input("/> ")
    end_time=time()
    actual_time=end_time-start_time
    actual_time=round(actual_time,2)
    user_input_list=user_input.split()
    if user_input==str:
        print("Perfect Accurecy!")
        print("WPS[Words/Second] ->",round(lenOf_words_str/actual_time,2),"wps")
        print("WPM[Words/Minutes] -> ",round(lenOf_words_str/(actual_time*0.0166667),2),"wpm")
        print("You typed",lenOf_words_str,"words.")
        print("You took",actual_time,"seconds.")
        i=input("Do you want to retest [y/n] : ").lower()
        if i=="y":
            continue
        elif i=="n":
            break
        else:
            exit()
            
    else:
        z=0
        try:
            for i in str_list:
                if i!=user_input_list[z]:
                    print("You had a mistake in",f"\'{i}\'[{z+1} No. word]")
                    user_input_list.remove(user_input_list[z])          #here!
                    lenOf_user_inputted_list=len(user_input_list)
                z+=1
        except IndexError as e:
            print("You didn't type accurately :",e)
        finally:
            print("WPS[Words/Second] ->",round(lenOf_user_inputted_list/actual_time,2),"wps")
            print("WPM[Words/Minutes] -> ",round(lenOf_user_inputted_list/(actual_time*0.0166667),2),"wpm")
            print("You typed",lenOf_user_inputted_list,"words correctly.")
            print("You took",actual_time,"seconds.")
            i=input("Do you want to retest [y/n] : ").lower()
            if i=="y":
                continue
            elif i=="n":
                break
            else:
                exit()

