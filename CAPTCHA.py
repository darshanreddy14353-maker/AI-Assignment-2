import random
import string

def generate_captcha(length=6):

    characters = string.ascii_letters + string.digits
    captcha = ''.join(random.choice(characters) for i in range(length))

    return captcha


captcha = generate_captcha()

print("CAPTCHA:", captcha)

user_input = input("Enter CAPTCHA: ")

if user_input == captcha:
    print("Human Verified")
else:
    print("Verification Failed")
