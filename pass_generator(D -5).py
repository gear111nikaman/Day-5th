import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '&', '(', ')', '+', '*']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


pass_letters = ""
for n in range(1 , nr_letters + 1):
    pass_letters += random.choice(letters)

pass_symb = ""
for i in range(1, nr_symbols + 1):
    pass_symb += random.choice(symbols)
    
pass_num = ""
for j in range(1, nr_numbers + 1):
    pass_num += random.choice(numbers)
    


password = pass_letters + pass_symb + pass_num
new_password = ""
for i in range(0, len(password) - 1):
    new_password += random.choice(password)

print(new_password)
