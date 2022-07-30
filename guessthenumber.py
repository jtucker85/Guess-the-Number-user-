import random

gr = False

b = 1
t = 1000

while gr == False:
    num = random.randint(b, t)
    ans = input(f"Is {num} too high (h), too low (l) or correct (c)?")
    if ans == "h":
        t = num - 1
    elif ans =="l":
        b = num + 1
    else:
        print(f"Wow! I am so awesome, right? You number was {num}.")
        gr = True