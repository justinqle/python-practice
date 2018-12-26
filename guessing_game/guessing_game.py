import random

bounds = (0, 101)   # tuple (inclusive, exclusive)
num = random.randint(bounds[0], bounds[1])
prompt = "Guess a number between %d and %d: " % (bounds[0], bounds[1] - 1)

while True:
    guess = int(input(prompt))
    if (guess < num):
        print("\nHigher!\n")
    elif(guess > num):
        print("\nLower!\n")
    else:
        break

print("\nYou got it!")
