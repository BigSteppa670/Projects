import random
# Welcome
print("Welcome to Your Password Generator")

# All random characters
randominus = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()"

# Amount of Generated Passwords
numba = input("Password Amount:")
numba = int(numba)
# Amount of Password Characters
length = input("Input Password Length:")
length = int(length)


print("\nHere are Your Passwords:")

for pwd in range(numba):
    passwords = ""
    for chars in range(length):
        passwords += random.choice(randominus)
    print(passwords)