import random

gr = False
count = 1
b = 1
t = 1000

print("Think of a number between 1 and 1000! I'm going to amaze you by guessing it.")

while gr != True:
    if b != t:
        num = random.randint(b, t)
    else:
        num = b
        count = count -1
        print(f"Your number is {num}, get rekt. It only took me {count} guesses!")
        quit()
    ans = input(f"I guess {num}! Is it too high (h), too low (l) or correct (c)?")
    if ans == "h":
        t = num - 1
        count = count +1
    elif ans =="l":
        b = num + 1
        count = count +1
    else:
        print(f"Wow! I am so awesome, right? Your number was {num}. And it only took me {count} guesses.")
        gr = True