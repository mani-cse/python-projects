import random
num = random.randint(1,20)
guess = int(input("Can you guess number its less than 20:"))
while num != guess:
    if guess > num:
        print("You guess is higher")
    else:
        print("You guess is lower")
        guess = int(input("guess again:"))
print("YOU WON!")