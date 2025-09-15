import random
import string   

password_length = 8

password_characters = string.ascii_letters + string.digits + string.punctuation

# list comprehension [function for i in rnage(n)]
# password ="".join([random.choice(password_characters) for i in range (password_length)])


password = ''
for i in range(password_length):
    password += random.choice(password_characters)

print("\nYour new password is:", password) 