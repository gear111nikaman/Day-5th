import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '&', '(', ')', '+', '*']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


pass_letters = ""
for n in range(0 , nr_letters):
    pass_letters += letters[random.randint(0, len(letters) - 1)]

pass_symb = ""
for i in range(0, nr_symbols):
    pass_symb += symbols[random.randint(0, len(symbols) - 1)]
    
pass_num = ""
for j in range(0, nr_numbers):
    pass_num += numbers[random.randint(0, len(numbers) - 1)]
    


password = pass_letters + pass_symb + pass_num
new_password = ""
for i in range(0, len(password) - 1):
    new_password += password[random.randint(0, len(password) - 1)]

print(new_password)
