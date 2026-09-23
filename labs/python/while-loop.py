import random

print("Welcome to guess the Number!")
print("The rules are simple. I will think of a number and you will try to guess it.")


number = random.randint(1,10)
isGuessRight = False


while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number :
        print(f"you guessed {guess}. That is correct! You win!")
        isGuessRight = True
    else:
        print(f"You guessed {guess}. Sorry, that isn't it. Try again.")

        
