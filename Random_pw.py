import random
import string
import secrets

letters=string.ascii_letters
numbers=string.digits

possible_char=letters+numbers

length=int(input("Pleaase Enter the size of the password: "))

password=" "
for num in range(length):
    password+=''.join(secrets.choice(possible_char))
    
print(password)