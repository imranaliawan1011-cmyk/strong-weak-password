import re

password = input("Enter password: ")

if (len(password) >= 8 and
    re.search(r"[a-z]", password) and
    re.search(r"[0-9]", password) and
    re.search(r"[@#$%&*!]", password)):
    print("Strong Password ")
else:
    print("Weak Password ")
print("Done")
print('Done2')