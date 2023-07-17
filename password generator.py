import random
import array


def numbers():
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    return random.choice(nums)


def low_letters():
    lower = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's',
             'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    return random.choice(lower)


def upp_letters():
    upper = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S',
             'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
    return random.choice(upper)


def special():
    special_char = ['!', '@', '#', '$', '%', '^', '&', '*',
                    '(', ')', '_', '+', '=', '/', '?', '}', '{', ']', '[', '|', '<', '>', ',', '.']
    return random.choice(special_char)


def password_gen(length_pass):
    password = ''
    i = 1

    while i <= length_pass:
        choice = random.randint(0, 3)
        if choice == 0:
            password += numbers()
        elif choice == 1:
            password += low_letters()
        elif choice == 2:
            password += upp_letters()
        else:
            password += special()
        i += 1
    return password


store_password = open('password.txt', 'a')
length_password = int(input("Enter the length of the password: "))
if(length_password >= 8):
    store_password.write("Length of the password : ")
    store_password.write(str(length_password))
    store_password.write('\t')
    store_password.write("Generated Password: ")
    store_password.write(password_gen(length_password))
    store_password.write('\n')
    # store_password.write("Generated Password : ",
    #                      password_gen(length_password))
else:
    while(length_password < 8):
        print("Length of the password should be atleast 8. Try again :(")
        length_password = int(input("Enter the length of the password: "))
    store_password.write("Length of the password : ")
    store_password.write(str(length_password))
    store_password.write('\t')
    store_password.write("Generated Password: ")
    store_password.write(password_gen(length_password))
    store_password.write('\n')
