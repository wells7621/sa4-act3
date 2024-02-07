
number = 10
num_guesses = 3

print("I'm thinking of a number...")
while num_guesses > 0:
    guess = input("What number am I thinking of? (Enter 'q' to quit): ")
    if guess == 'q':
        print(f"Sorry! The number was {number}.")
        break
    guess = int(guess)
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        num_guesses -= 1
        print(f"Sorry! Try again. You have {num_guesses} guesses left. ")
        if num_guesses == 0:
            print(f"Sorry! The number was {number}.")


