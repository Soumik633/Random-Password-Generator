import random
import string


characters = string.ascii_letters + string.digits

length = 10  

password = ""

for _ in range(length):
    password += random.choice(characters)

print("Your password is:", password)
