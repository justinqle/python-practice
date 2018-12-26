import random

bounds = (0, 101)   # tuple (inclusive, exclusive)
num = random.randint(bounds[0], bounds[1])
prompt = f"Guess a number between {bounds[0]} and {bounds[1]-1}: "

while True:
    try:
        guess = int(input(prompt))
        if (guess < bounds[0] or guess >= bounds[1]):
            raise ValueError
    except ValueError:
        print("Oops! Please enter a valid number.")
    except KeyboardInterrupt as err:
        print(err)
        exit()
    else:
        if guess < num:
            print("Higher!")
        elif guess > num:
            print("Lower!")
        else:
            break

print("You got it!")
