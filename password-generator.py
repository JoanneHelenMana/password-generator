import random
import string

password = []
length = 10

for i in range(length):
    randomCharacter = random.choice(string.ascii_letters)
    password.append(randomCharacter)

print(f"Password: {''.join(password)}")
