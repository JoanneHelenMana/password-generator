import random
import string
from passwordstrength.passwordmeter import PasswordStrength


passwordList = []
characters = []
lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
digits = list(string.digits)
specialCharacters = list(string.punctuation)

while True:
    length = int(input(f"What's the required length of your password? Enter a number between 1 and 50: "))

    if 0 < length <= 50:

        print(f"\nReply 'yes' or 'no' to include your password requirements.\n")

        inputLowercase = str(input(f"Does your password require lowercase?: "))
        if inputLowercase == 'yes':
            characters += lowercase

        inputUppercase = str(input(f"Does your password require uppercase?: "))
        if inputUppercase == 'yes':
            characters += uppercase

        inputDigits = str(input(f"Does your password require digits?: "))
        if inputDigits == 'yes':
            characters += digits

        inputSpecialCharacters = str(input(f"Does your password require special characters?: "))
        if inputSpecialCharacters == 'yes':
            characters += specialCharacters

        for i in range(length):
            randomCharacter = random.choice(characters)
            passwordList.append(randomCharacter)
        break

    elif length <= 0 or length > 50:
        print("Number out of range.")

password = ''.join(passwordList)
print(f"\nPassword generated: {password}")

strength = PasswordStrength(password)
print(f"Rating: {strength.rating()}")
