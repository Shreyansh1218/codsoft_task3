import random
import string


lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special_chars = string.punctuation

letters=lowercase+uppercase

print("Welcome To Password Generator")
letters_n=int(input("How many letters do you want in your password?\n"))
symbols_n=int(input("How many symbols do you want in your password?\n"))
digits_n=int(input("How many digits do you want in your password?\n"))
password_list=[]

for i in range(1,letters_n+1):
    generated=random.choice(letters)
    password_list += generated   

for i in range(1,digits_n+1):
    generated=random.choice(digits)
    password_list += generated

for i in range(1,symbols_n+1):
    generated=random.choice(special_chars)
    password_list += generated


random.shuffle(password_list)

password=""

for gen in password_list:
    password += gen

print("Thankyou!! , Your Password Has Been Generated")
print("GENERATED PASSWORD:- ",password)

    

