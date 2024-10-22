### Part Two -- your code goes here. 
import random 

secret_number = random.randint(1, 100)
guess = ""

while guess != secret_number:
    guess = int(input("Please guess a number between 1 and 100 :"))
    if guess > secret_number:
       print("You're too high! Guess again")
    elif guess < secret_number:
       print("You're too low! Guess again") 
    else:
       print("Congarts! You guessed the right number.")