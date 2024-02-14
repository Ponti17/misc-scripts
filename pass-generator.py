import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cap_letters = [letter.upper() for letter in letters]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
chars = ['!', '(', ')', '-', '_']

passw = []
pass_length = 12

for letter in range(0, pass_length-6):
    if random.randint(0, 1) == 0:
        passw.append(letters[random.randint(0, len(letters) - 1)])
    else:
        passw.append(cap_letters[random.randint(0, len(cap_letters) - 1)])
for num in range(0, 4):
    passw.append(numbers[random.randint(0, len(numbers) - 1)])
for char in range(0, 2):
    passw.append(chars[random.randint(0, len(chars) - 1)])

passw = ''.join(passw)

print("Password: " + passw)

while(True):
    save = input("Save password in .txt file? (Y/N): ")
    if save.lower() == 'y':
        with open('recent-pass.txt', 'w') as f:
            f.write(passw)
            exit()
    elif save.lower() != 'n':
        print("Invalid input.\n")
    else:
        exit()
