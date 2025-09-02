import random
import time
import string
import getpass

def strong(password):
    if len(password) <= 14:
        return False
    
    symbols = sum(1 for ch in password if ch in string.punctuation)
    letters = sum(1 for ch in password if ch in string.ascii_letters)
    digits = sum(1 for ch in password if ch in string.digits)

    return symbols >= 3 and letters >= 3 and digits >= 3

def good(password):
    if len(password) <= 11:
        return False
    
    symbols = sum(1 for ch in password if ch in string.punctuation)
    letters = sum(1 for ch in password if ch in string.ascii_letters)
    digits = sum(1 for ch in password if ch in string.digits)

    return symbols >= 2 and letters >= 3 and digits >= 2

def weak(password):
    if len(password) <= 8:
        return False
    symbols = sum(1 for ch in password if ch in string.punctuation)
    letters = sum(1 for ch in password if ch in string.ascii_letters)
    digits = sum(1 for ch in password if ch in string.digits)

    return symbols >= 1 and letters >= 2 and digits >= 1


def password_generator():
    password = []
    print()
    print("You have selected to generate a password, one moment please...")

    symbols_amount = random.randint(4, 6)
    l_letters_amount = random.randint(5, 6)
    u_letters_amount = random.randint(5, 6)
    digits_amount = random.randint(4, 6)
    symbols = random.sample(string.punctuation, len(string.punctuation))
    l_letters = random.sample(string.ascii_lowercase, len(string.ascii_lowercase))
    u_letters = random.sample(string.ascii_uppercase, len(string.ascii_uppercase))
    digits = random.sample(string.digits, len(string.digits))


    for x in range(symbols_amount):
        password += symbols[x]
    for x in range(l_letters_amount):
        password += l_letters[x]
    for x in range(u_letters_amount):
        password += u_letters[x]
    for x in range(digits_amount):
        password += digits[x]
    
    random.shuffle(password)
    final_password = "".join(password)

    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print()

    print(f"your generated password is {final_password}")
    print()

def password_strength():
    print()
    print("READ THIS FIRST BEFORE TYPING ANYTHING")
    print("Recommendations for a good password:")
    print("- Atleast 14 characters")
    print("- Use a combination of uppercase and lowercase letters, numbers and symbols")
    print("- Do not use any (easy to guess) words (birthplace, a country/city, your own name, commonly used words,...)")
    print("- If your password is under 14 characters consider changing it every few months/years for 100 percent safety")
    print("You will NOT be able to see what you type in, make sure you type the correct password")
    print()
    password = getpass.getpass("Please enter your password: ")
    print()
    print("Let's see...")
    time.sleep(1)
    if strong(password):
        print("You have a great password! It is very unlikely your password will ever be guessed")
    elif good(password):
        print("You have a good and secure password! A few extra characters would make it a LOT stronger though")
    elif weak(password):
        print("Your password is weak, consider the following:")
        print("- Aim for 14+ characters")
        print("- Use a combination of uppercase and lowercase letters, numbers and symbols")
        print("- Do not use any (easy to guess) words") 
    else:
        print("Never use this password as it is very easy to guess and a hacker can instantly figure out what it is")
        print("Please consider the following:")
        print("- Aim for 14+ characters")
        print("- Use a combination of uppercase and lowercase letters, numbers and symbols")
        print("- Do not use any (easy to guess) words") 

def main():
    print("Welcome to the password generator and strength checker!")
    while True:
        
        print()
        print("Please select what you would like to do")
        print("1. Generate a strong password")
        print("2. Check the strength of a password")
        print("3. Exit")
        print()
        option = input("Choose 1, 2 or 3: ")

        match option:
            case '1':
                password_generator()
                print()
            case '2':
                password_strength()
                print()
            case '3':
                print()
                break
            case _:
                print("Sorry, that is not a valid option")
                print()
    print("Thanks for using my password generator! Have a nice day!")

if __name__ == "__main__":
    main()