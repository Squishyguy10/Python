import requests
import sys
from random import choice

def canvas(wrong):
    print("     ______")
    print("    |      |")
    print("    |      |")
    if wrong == 0:
        print("    |")
        print("    |")
        print("    |")
    elif wrong == 1:
        print("    |      0")
        print("    |")
        print("    |")
    elif wrong == 2:
        print("    |      0")
        print("    |      |")
        print("    |")
    elif wrong == 3:
        print("    |      0")
        print("    |     /|")
        print("    |")
    elif wrong == 4:
        print("    |      0")
        print("    |     /|\\")
        print("    |")
    elif wrong == 5:
        print("    |      0")
        print("    |     /|\\")
        print("    |     /")
    elif wrong == 6:
        print("    |      0")
        print("    |     /|\\")
        print("    |     / \\")
    print("    |")
    print("____|____")

url = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(url)
# print(response.text)

# WORDS = response.text.splitlines()
with open("wordlist.10000.txt", "w") as w_file:
    w_file.write(response.text)
with open("wordlist.10000.txt", "r") as r_file:
    global WORDS
    WORDS = r_file.readlines()

min_length = 5

pick = choice(WORDS)
while len(pick) < min_length:
    pick = choice(WORDS)
print(pick)

userword = ""
for i in range(len(pick)-1):
    userword += "_"

wrong = 0
while('_' in userword):
    canvas(wrong)
    if wrong < 6:
        for chr_element in userword:
            print(chr_element, end = " ")
        guess = input("\nInput a character:\n")
        if guess in pick:
            for i in range(len(pick)):
                if guess == pick[i]:
                    list_userword = list(userword)
                    list_userword[i] = guess
                    userword = ''.join(list_userword)
        else:
            wrong+= 1
    else:
        print("You Lost\nThe word was", pick)
        sys.exit()
print(userword)
print("You Win")