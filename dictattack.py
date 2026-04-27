import hashlib
from winsound import Beep

def cracked(hash_from_user,file_name,hash_type):
    i=0

    list_of_matched_passwords = []
    try:
        f=open(file_name,"r")
    except FileNotFoundError as e:
        print("File_not_found :",e)
        print("Programme_exitted!")
        exit()
    full_text=f.read()
    list_of_text=full_text.split()
    for password in list_of_text:
        i+=1
        dp=password.encode()
        if hash_type == 1:
            dp = hashlib.md5(dp)
        elif hash_type == 2:
            dp = hashlib.sha256(dp)
        elif hash_type == 3:
            dp = hashlib.sha1(dp)
        elif hash_type == 4:
            dp = hashlib.sha224(dp)
        elif hash_type == 5:
            dp = hashlib.sha384(dp)
        elif hash_type == 6:
            dp = hashlib.sha3_256(dp)
        elif hash_type == 7:
            dp = hashlib.sha3_224(dp)
        elif hash_type == 8:
            dp = hashlib.sha3_512(dp)
        elif hash_type == 9:
            dp = hashlib.sha512()
        elif hash_type == 10:
            dp = hashlib.blake2b(dp)
        

        hashes_from_file = dp.hexdigest()
        if hashes_from_file == hash_from_user:
            Beep(1000,200)
            Beep(1000,200)
            print("Password found :",password,"\nLine No:",i)
            list_of_matched_passwords.append(f"Password found : {password}\nLine No: {i}")
        else:
            print("Password_did_not_match_:",password+"\nHash :",hashes_from_file)
    if len(list_of_matched_passwords)>=1:
        print("____________________________________________")
        for sup in list_of_matched_passwords:
            print(sup)
        print("____________________________________________")
    else:
        print("____________________________________________")
        print("Password_wasn't_found_in :",file_name)
        print("____________________________________________")
    # file_name.close()

list_of_hashes_available = ["MD5","SHA256","SHA1","SHA224","SHA384","SHA3_256","SHA3_224","SHA3_512","SHA512","BLAKE_2B"]
print("Available_Hash_Types: ")
for index,item in enumerate(list_of_hashes_available):
    print(index+1 ,":", item)
try:
    user_hash_type = int(input("Enter_Hash_Type_: "))
except ValueError:
    print("Enter_an_int_value\nProgramme_quit!")
    quit()
user = input(f"Enter_{list_of_hashes_available[user_hash_type-1]}_hashed_password_: \n").strip()
user_file = input("Enter_filename_of_the_passwords_: ")
cracked(user,user_file,user_hash_type)
i
