import random
import string
print('Welcome to Random Password Generator')
a = string.ascii_letters #a-z A-Z
b = string.digits #0-9
c = string.punctuation #special character

all_characters =a+b+c
length = 15 # You can change the desired length of the password here
password = ""

for i in range(length):
  password += random.choice(all_characters)

print('Generated Password: ',password)
