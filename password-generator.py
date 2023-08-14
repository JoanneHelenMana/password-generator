import random
import string

password = []

while True:
    length = int(input(f"What's the required length of your password? Enter a number between 1 and 50: "))

    if 0 < length <= 50:
        for i in range(length):
            randomCharacter = random.choice(string.ascii_letters)
            password.append(randomCharacter)
        break

    elif length <= 0 or length > 50:
        print("Number out of range.")

print(f"Password: {''.join(password)}")
