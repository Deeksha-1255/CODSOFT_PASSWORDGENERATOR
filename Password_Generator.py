import random

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = lowercase_letters.upper()
digits = "0123456789"
symbols = "!@#$%^&*()_+{}[]?,. "

upper,lower,number,symbol = True,True,False,False

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if number:
    all += digits
if symbol:
    all += symbols
    
length = 6
amount = 2
for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)