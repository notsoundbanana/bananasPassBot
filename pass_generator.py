import random


def main(n):
    symbols = "qwertyuiop[]asdfghjkl\zxcvbnm/1234567890!#*()_QWERTYUIOP{}ASDFGHJKLZXCVBNM<>?"
    password = ""
    password += str(symbols[random.randint(0, len(symbols) - 1)])
    for _ in range(n-1):
        a = random.randint(0, len(symbols) - 1)
        while symbols[a] == password[-1]:
            a = random.randint(0, len(symbols) - 1)
        password += str(symbols[a])
    return password